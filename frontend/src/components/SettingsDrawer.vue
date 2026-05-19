<template>
  <el-drawer
    v-model="visible"
    title="设置"
    direction="ltr"
    size="360px"
    :append-to-body="true"
  >
    <div class="settings-panel">
      <div class="settings-section">
        <div class="settings-section-title">
          <Settings :size="16" />
          <span>解析设置</span>
        </div>
        <div class="settings-form">
          <div class="settings-form-item">
            <label>后端引擎</label>
            <el-select v-model="localConfig.backend" placeholder="请选择" style="width: 100%">
              <el-option label="Pipeline (通用)" value="pipeline" />
              <el-option label="VLM Auto Engine (高精度)" value="vlm-auto-engine" />
              <el-option label="Hybrid Auto Engine (混合)" value="hybrid-auto-engine" />
            </el-select>
          </div>
          <div class="settings-form-item">
            <label>解析方法</label>
            <el-select v-model="localConfig.parseMethod" placeholder="请选择" style="width: 100%">
              <el-option label="Auto (自动)" value="auto" />
              <el-option label="Text (纯文本)" value="txt" />
              <el-option label="OCR (光学识别)" value="ocr" />
            </el-select>
          </div>
          <div class="settings-form-item">
            <label>语言</label>
            <el-select v-model="localConfig.lang" placeholder="请选择" style="width: 100%">
              <el-option label="中文" value="ch" />
              <el-option label="中文(轻量)" value="ch_lite" />
              <el-option label="英文" value="en" />
              <el-option label="日语" value="japan" />
              <el-option label="韩语" value="korean" />
              <el-option label="繁体中文" value="chinese_cht" />
              <el-option label="泰语" value="th" />
              <el-option label="阿拉伯语" value="arabic" />
              <el-option label="俄语" value="east_slavic" />
            </el-select>
          </div>
          <div class="settings-form-item">
            <label>页码范围</label>
            <div class="range-input">
              <el-input
                v-model.number="localConfig.startPage"
                placeholder="起始页"
                type="number"
                :min="0"
                class="range-field"
              />
              <span class="range-separator">-</span>
              <el-input
                v-model.number="localConfig.endPage"
                placeholder="结束页"
                type="number"
                :min="0"
                class="range-field"
              />
            </div>
          </div>
          <div class="settings-form-item">
            <label>功能开关</label>
            <div class="switch-group">
              <el-switch v-model="localConfig.formulaEnable" active-text="公式解析" inactive-text="公式" />
              <el-switch v-model="localConfig.tableEnable" active-text="表格解析" inactive-text="表格" />
              <el-switch v-model="localConfig.imageAnalysis" active-text="图片/图表分析" inactive-text="图片" />
            </div>
          </div>
          <div class="settings-form-item">
            <button class="reset-btn" @click="resetConfig">
              <RotateCcw :size="16" />
              重置配置
            </button>
          </div>
        </div>
      </div>

      <div class="settings-section">
        <div class="settings-section-title">
          <Cpu :size="16" />
          <span>AI 模型设置</span>
        </div>
        <div class="settings-form">
          <div class="settings-form-item">
            <label>API URL</label>
            <el-input
              v-model="aiSettingsStore.apiUrl"
              placeholder="http://localhost:8000/v1"
            />
          </div>
          <div class="settings-form-item">
            <label>API Key</label>
            <el-input
              v-model="aiSettingsStore.apiKey"
              type="password"
              placeholder="请输入 API Key"
              show-password
            />
          </div>
          <div class="settings-form-item">
            <label>模型名称</label>
            <el-input
              v-model="aiSettingsStore.modelName"
              placeholder="如 qwen2.5-7b-instruct"
            />
          </div>
          <div class="settings-form-item">
            <label>自定义提示词</label>
            <el-input
              v-model="aiSettingsStore.prompt"
              type="textarea"
              :rows="4"
              placeholder="请输入自定义提示词"
            />
          </div>
          <button
            class="parse-btn save-settings-btn"
            @click="handleSaveSettings"
            :disabled="aiSettingsStore.isSaving"
          >
            <Loader2 v-if="aiSettingsStore.isSaving" :size="18" class="spin" />
            {{ aiSettingsStore.isSaving ? '保存中...' : '保存设置' }}
          </button>
        </div>
      </div>
    </div>
  </el-drawer>
</template>

<script setup>
import { reactive, watch } from 'vue';
import { Settings, Cpu, Loader2, RotateCcw } from 'lucide-vue-next';
import { ElMessage } from 'element-plus';
import { useConfigStore } from '../stores/configStore';
import { useAiSettingsStore } from '../stores/aiSettings';

const visible = defineModel({ type: Boolean, default: false });

const configStore = useConfigStore();
const aiSettingsStore = useAiSettingsStore();

const localConfig = reactive({
  backend: configStore.backend,
  parseMethod: configStore.parseMethod,
  lang: configStore.lang,
  startPage: configStore.startPage,
  endPage: configStore.endPage,
  formulaEnable: configStore.formulaEnable,
  tableEnable: configStore.tableEnable,
  imageAnalysis: configStore.imageAnalysis,
  asyncMode: configStore.asyncMode,
  returnImages: configStore.returnImages,
});

watch(localConfig, (newConfig) => {
  configStore.updateConfig(newConfig);
}, { deep: true });

const resetConfig = () => {
  configStore.resetConfig();
  Object.assign(localConfig, {
    backend: configStore.backend,
    parseMethod: configStore.parseMethod,
    lang: configStore.lang,
    startPage: configStore.startPage,
    endPage: configStore.endPage,
    formulaEnable: configStore.formulaEnable,
    tableEnable: configStore.tableEnable,
    imageAnalysis: configStore.imageAnalysis,
    asyncMode: configStore.asyncMode,
    returnImages: configStore.returnImages,
  });
};

const handleSaveSettings = async () => {
  try {
    await aiSettingsStore.saveToServer();
    ElMessage.success('设置已保存');
  } catch (err) {
    ElMessage.error(err.message || '保存设置失败');
  }
};
</script>

<style scoped>
.settings-panel {
  padding: 0 4px;
}

.settings-section {
  margin-bottom: 28px;
}

.settings-section-title {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 15px;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 16px;
  padding-bottom: 10px;
  border-bottom: 1px solid #f3f4f6;
}

.settings-section-title svg {
  color: #0288d1;
}

.settings-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.settings-form-item {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.settings-form-item label {
  font-size: 13px;
  color: #6b7280;
  font-weight: 500;
}

.range-input {
  display: flex;
  align-items: center;
  gap: 10px;
}

.range-field {
  flex: 1;
}

.range-separator {
  color: #999;
}

.switch-group {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.mode-hint {
  display: block;
  font-size: 12px;
  color: #faad14;
  margin-top: 4px;
}

.reset-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  border: 1px solid #d9d9d9;
  border-radius: 6px;
  font-size: 13px;
  cursor: pointer;
  transition: all 0.2s;
  background-color: #fff;
  color: #666;
  width: fit-content;
}

.reset-btn:hover {
  background-color: #f5f5f5;
  border-color: #1890ff;
  color: #1890ff;
}

.save-settings-btn {
  margin-top: 4px;
}
</style>
