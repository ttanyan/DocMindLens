import { defineStore } from 'pinia';

const DEFAULT_PROMPT = '请将以下文档内容总结为层次分明的 Markdown 格式，使用 # ## ### 等标题层级组织内容，保留关键信息，去除冗余细节。输出纯 Markdown，不要包含其他说明。';

const baseURL = import.meta.env.VITE_MINERU_API_URL || 'http://localhost:8000';

export const useAiSettingsStore = defineStore('aiSettings', {
  state: () => ({
    apiUrl: '',
    apiKey: '',
    modelName: '',
    prompt: DEFAULT_PROMPT,
    isLoaded: false,
    isSaving: false,
  }),

  getters: {
    isConfigured: (state) => !!(state.apiUrl && state.apiKey && state.modelName),
  },

  actions: {
    async loadFromServer() {
      try {
        const resp = await fetch(`${baseURL}/api/ai-settings`);
        if (resp.ok) {
          const data = await resp.json();
          this.apiUrl = data.api_url || '';
          this.apiKey = data.api_key || '';
          this.modelName = data.model || '';
          this.prompt = data.prompt || DEFAULT_PROMPT;
          this.isLoaded = true;
        }
      } catch (_) {}
    },

    async saveToServer() {
      this.isSaving = true;
      try {
        const resp = await fetch(`${baseURL}/api/ai-settings`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            api_url: this.apiUrl,
            api_key: this.apiKey,
            model: this.modelName,
            prompt: this.prompt,
          }),
        });
        if (!resp.ok) {
          const err = await resp.json().catch(() => ({}));
          throw new Error(err.detail || '保存失败');
        }
        return true;
      } catch (err) {
        console.error('保存 AI 设置失败:', err);
        throw err;
      } finally {
        this.isSaving = false;
      }
    },
  },
});
