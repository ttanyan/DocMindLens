import { ref } from 'vue';
import { useAiSettingsStore } from '../stores/aiSettings';

const baseURL = import.meta.env.VITE_MINERU_API_URL || 'http://localhost:8000';

const summaryCache = new Map();
const isSummarizing = ref(false);
const summaryError = ref('');
const currentSummary = ref('');

export function useAiSummarize() {
  const aiSettings = useAiSettingsStore();

  const fetchSummary = async (taskId, markdownContent, forceRefresh = false) => {
    if (!aiSettings.isConfigured) {
      summaryError.value = '请先在侧边栏配置 AI 模型设置';
      return '';
    }

    if (!forceRefresh && summaryCache.has(taskId)) {
      currentSummary.value = summaryCache.get(taskId);
      return currentSummary.value;
    }

    isSummarizing.value = true;
    summaryError.value = '';
    currentSummary.value = '';

    try {
      const response = await fetch(`${baseURL}/api/ai-summarize`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          markdown: markdownContent,
          api_url: aiSettings.apiUrl,
          api_key: aiSettings.apiKey,
          prompt: aiSettings.prompt,
          model: aiSettings.modelName || 'default',
        }),
      });

      if (!response.ok) {
        const errData = await response.json().catch(() => ({}));
        throw new Error(errData.detail || `请求失败 (${response.status})`);
      }

      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let accumulated = '';
      let buffer = '';

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split('\n');
        buffer = lines.pop() || '';

        for (const line of lines) {
          const trimmed = line.trim();
          if (!trimmed || !trimmed.startsWith('data: ')) continue;
          const data = trimmed.slice(6);
          if (data === '[DONE]') continue;

          try {
            const parsed = JSON.parse(data);
            if (parsed.error) {
              summaryError.value = parsed.error;
              break;
            }
            if (parsed.content) {
              accumulated += parsed.content;
              currentSummary.value = accumulated;
            }
          } catch (_) {}
        }
      }

      if (accumulated && !summaryError.value) {
        summaryCache.set(taskId, accumulated);
        currentSummary.value = accumulated;
      }
    } catch (err) {
      summaryError.value = err.message || 'AI 总结请求失败';
    } finally {
      isSummarizing.value = false;
    }

    return currentSummary.value;
  };

  const clearCache = (taskId) => {
    if (taskId) {
      summaryCache.delete(taskId);
    } else {
      summaryCache.clear();
    }
  };

  const getCachedSummary = (taskId) => {
    return summaryCache.get(taskId) || '';
  };

  const hasCachedSummary = (taskId) => {
    return summaryCache.has(taskId);
  };

  return {
    isSummarizing,
    summaryError,
    currentSummary,
    fetchSummary,
    clearCache,
    getCachedSummary,
    hasCachedSummary,
  };
}
