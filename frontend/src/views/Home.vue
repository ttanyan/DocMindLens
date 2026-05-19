<template>
  <div class="app-container">
    <aside class="sidebar" :class="{ collapsed: sidebarCollapsed }">
      <div class="sidebar-header">
        <div class="logo">
          <component :is="logoIcon" :size="24" />
          <span v-if="!sidebarCollapsed" class="logo-text">DocMindLens</span>
        </div>
        <button class="collapse-btn" @click="sidebarCollapsed = !sidebarCollapsed">
          <PanelLeftClose v-if="!sidebarCollapsed" :size="18" />
          <PanelLeftOpen v-else :size="18" />
        </button>
      </div>

      <nav class="sidebar-nav">
        <button class="nav-item active" @click="handleNewParse">
          <PlusCircle :size="20" />
          <span v-if="!sidebarCollapsed">新解析</span>
        </button>
      </nav>

      <div v-if="!sidebarCollapsed" class="sidebar-divider"></div>

      <div class="task-list" :class="{ collapsed: sidebarCollapsed }">
        <div v-if="!sidebarCollapsed" class="task-list-header">
          <div class="task-search">
            <Search :size="14" />
            <input
              v-model="searchQuery"
              type="text"
              class="search-input"
              placeholder="搜索任务..."
            />
          </div>
        </div>
        <div class="task-list-content" :class="{ collapsed: sidebarCollapsed }">
          <div
            v-for="(task, index) in filteredTasks"
            :key="task.task_id || index"
            class="task-item"
            :class="{ active: selectedTask?.task_id === task.task_id }"
            :title="sidebarCollapsed ? (task.name || task.file_names?.[0] || '未知文件') : ''"
            @click="selectTask(task)"
          >
            <img
              :src="getFileIcon(task.file_names?.[0])"
              class="task-file-icon"
              :class="{ 'collapsed-icon': sidebarCollapsed }"
              alt=""
            />
            <span v-if="!sidebarCollapsed" class="task-name">{{ task.name || task.file_names?.[0] || '未知文件' }}</span>
            <span v-else class="task-name-collapsed">{{ (task.name || task.file_names?.[0] || '未知').slice(0, 2) }}</span>
            <button
              v-if="!sidebarCollapsed"
              class="task-delete-btn"
              @click.stop="handleDeleteTask(task)"
              title="删除任务"
            >
              <Trash2 :size="14" />
            </button>
          </div>
        </div>
      </div>

      <div class="sidebar-footer">
        <button class="nav-item settings-btn" @click="settingsDrawerVisible = true">
          <Settings :size="20" />
          <span v-if="!sidebarCollapsed">设置</span>
        </button>
      </div>
    </aside>

    <main class="main-area" @click="closeTaskList">
      <header v-if="!selectedTask" class="top-header">
        <div class="header-left">
          <h1 class="page-title">DocMindLens</h1>
          <span class="page-subtitle-tag">{{ typedText }}</span>
        </div>
      </header>

      <header v-else class="top-header">
        <div class="header-left">
          <button class="back-btn" @click="selectedTask = null">
            <ArrowLeft :size="18" />
          </button>
          <h1 class="page-title">{{ selectedTask.name || selectedTask.file_names?.[0] }}</h1>
        </div>
      </header>

      <div v-if="!selectedTask" class="parse-area">
        <div
          class="upload-dropzone"
          :class="{ 'drag-over': isDragOver }"
          @dragover.prevent="onDragOver"
          @dragleave.prevent="onDragLeave"
          @drop.prevent="handleDrop"
        >
          <svg class="upload-cloud-icon" :class="{ uploaded: selectedFiles.length > 0 }" width="160" height="80" viewBox="0 0 101 51" fill="none" xmlns="http://www.w3.org/2000/svg">
<g :class="['side-icon-left', selectedFiles.length === 0 || getFileTypes.xls ? 'active' : 'inactive']" clip-path="url(#clip0_16490_20150)">
<path d="M9.67846 25.7419C9.72166 25.4579 9.87593 25.2026 10.1073 25.0323L16.9547 19.9927C18.2397 19.0469 20.048 19.322 20.9938 20.6069L30.412 33.4036C31.3577 34.6885 31.0827 36.4969 29.7978 37.4426L20.4911 44.2922C19.2061 45.238 17.3978 44.963 16.4521 43.678L8.84382 33.3406C8.67351 33.1092 8.6021 32.8196 8.6453 32.5356L9.67846 25.7419Z" fill="#71A3FA"/>
<path d="M10.1201 25.0234L10.0453 25.0785C9.81387 25.2488 9.6596 25.5041 9.6164 25.7881L8.59961 32.4741C8.55641 32.7582 8.62782 33.0478 8.79813 33.2792L8.85322 33.354C8.67589 33.1131 8.72746 32.774 8.96839 32.5967L12.1411 30.2616C12.5573 29.9553 12.6463 29.3696 12.34 28.9535L10.0049 25.7808C9.82762 25.5398 9.87918 25.2008 10.1201 25.0234Z" fill="#8ABDFF"/>
<path d="M16.454 33.0084C17.1768 32.4765 17.3314 31.4593 16.7995 30.7365C16.2675 30.0137 15.2503 29.859 14.5275 30.391C13.8047 30.9229 13.65 31.9401 14.182 32.6629C14.714 33.3857 15.7311 33.5404 16.454 33.0084Z" fill="white"/>
<path d="M26.9471 33.0547C27.5153 33.3091 27.5981 34.0816 27.0967 34.4506L19.318 40.1756C18.8145 40.5462 18.0986 40.2331 18.029 39.6118L17.64 36.1424C17.5717 35.5327 18.1778 35.0702 18.7478 35.297L19.1626 35.462C19.735 35.6897 20.3428 35.2225 20.2698 34.6108L19.8668 31.2321C19.792 30.6053 20.4294 30.1364 21.0056 30.3943L26.9471 33.0547Z" fill="white"/>
</g>
<g :class="['side-icon-right', selectedFiles.length === 0 || getFileTypes.doc ? 'active' : 'inactive']" clip-path="url(#clip1_16490_20150)">
<path d="M85.7918 21.335C86.0732 21.277 86.3661 21.3332 86.6061 21.4912L93.7078 26.1656C95.0405 27.0428 95.4097 28.8343 94.5325 30.167L85.7968 43.4389C84.9196 44.7716 83.1281 45.1409 81.7954 44.2637L72.1431 37.9104C70.8104 37.0332 70.4411 35.2417 71.3183 33.909L78.3753 23.1877C78.5332 22.9477 78.7801 22.7803 79.0615 22.7223L85.7918 21.335Z" fill="#AFEDD0"/>
<path d="M86.6194 21.499L86.5418 21.4479C86.3018 21.29 86.0088 21.2338 85.7274 21.2918L79.1038 22.6571C78.8224 22.7151 78.5756 22.8825 78.4176 23.1225L78.3665 23.2001C78.531 22.9502 78.8669 22.881 79.1168 23.0454L82.4073 25.2113C82.8389 25.4954 83.4191 25.3758 83.7032 24.9442L85.8691 21.6537C86.0336 21.4038 86.3695 21.3345 86.6194 21.499Z" fill="#B3F5CF"/>
<g clip-path="url(#clip2_16490_20150)">
<path d="M86.2217 32.6842L86.0523 31.8622L81.2603 28.708L82.2769 33.6402L77.3447 34.6568L82.1368 37.811L82.9588 37.6415" stroke="white" stroke-width="1.4837" stroke-linecap="square" stroke-linejoin="round"/>
</g>
</g>
<g :class="['side-icon-right', selectedFiles.length === 0 || getFileTypes.image ? 'active' : 'inactive']" clip-path="url(#clip3_16490_20150)">
<path d="M71.7766 9.94136C72.1533 9.81339 72.5654 9.84029 72.9223 10.0162L83.4816 15.2201C85.4632 16.1966 86.2779 18.5947 85.3014 20.5762L75.5761 40.3099C74.5996 42.2915 72.2015 43.1062 70.2199 42.1297L55.8681 35.0568C53.8866 34.0802 53.0719 31.6822 54.0484 29.7006L61.9047 13.7593C62.0805 13.4025 62.3909 13.1301 62.7676 13.0021L71.7766 9.94136Z" fill="#71A3FA"/>
<path d="M72.9419 10.0264L72.8265 9.96948C72.4696 9.79362 72.0575 9.76672 71.6809 9.89469L62.8146 12.9069C62.4379 13.0349 62.1275 13.3073 61.9517 13.6641L61.8948 13.7795C62.0779 13.408 62.5275 13.2552 62.8991 13.4384L67.7917 15.8496C68.4335 16.1658 69.2101 15.902 69.5264 15.2602L71.9376 10.3676C72.1207 9.99602 72.5704 9.84326 72.9419 10.0264Z" fill="#8ABDFF"/>
<path d="M66.5287 20.4346L65.2314 26.9336L69.9488 22.1201L71.7886 23.0268L70.8451 29.7002L75.2087 24.7123L77.6264 25.9038L70.5905 33.4883L68.2318 32.3259L69.0263 26.312L64.741 30.6055L62.3823 29.4431L64.1111 19.2432L66.5287 20.4346Z" fill="white"/>
</g>
<g :class="['side-icon-left', selectedFiles.length === 0 || getFileTypes.ppt ? 'active' : 'inactive']" clip-path="url(#clip4_16490_20150)">
<path d="M21.8381 14.2725C22.0016 13.9098 22.3024 13.627 22.6745 13.4861L33.6838 9.31773C35.7498 8.53549 38.0588 9.5762 38.841 11.6422L46.631 32.2169C47.4133 34.2829 46.3725 36.5918 44.3065 37.3741L29.3432 43.0395C27.2771 43.8217 24.9682 42.781 24.1859 40.715L17.893 24.0944C17.7522 23.7224 17.7649 23.3096 17.9284 22.9469L21.8381 14.2725Z" fill="#FEA581"/>
<path d="M22.6951 13.4785L22.5747 13.5241C22.2027 13.6649 21.9018 13.9478 21.7383 14.3105L17.8906 22.8474C17.7271 23.2101 17.7144 23.6229 17.8553 23.9949L17.9008 24.1153C17.7541 23.7279 17.9493 23.2949 18.3367 23.1483L23.4378 21.2169C24.1069 20.9635 24.444 20.2158 24.1906 19.5466L22.2592 14.4455C22.1126 14.0581 22.3077 13.6252 22.6951 13.4785Z" fill="#FFBB96"/>
<path d="M30.9933 27.9351L31.8882 27.5963C32.8794 27.221 33.2117 26.602 32.8851 25.7393C32.5584 24.8765 31.8995 24.6328 30.9083 25.0081L30.0134 25.3469L30.9933 27.9351ZM33.12 33.5521L30.4217 34.5738L26.4915 24.1934L30.7868 22.5671C31.9524 22.1257 32.9574 22.0915 33.8016 22.4645C34.6551 22.8339 35.2903 23.5693 35.7073 24.6707C36.1243 25.7721 36.1355 26.7438 35.7407 27.5858C35.3551 28.4244 34.5795 29.0644 33.4139 29.5057L31.8169 30.1103L33.12 33.5521Z" fill="white"/>
</g>
<g :class="['main-icon', selectedFiles.length === 0 || getFileTypes.pdf ? 'active' : 'inactive']">
<path d="M44.7864 4.58383C45.1614 4.20876 45.6702 3.99805 46.2006 3.99805H61.8966C64.8422 3.99805 67.23 6.38586 67.23 9.33138V38.6647C67.23 41.6102 64.8422 43.998 61.8966 43.998H40.5633C37.6178 43.998 35.23 41.6102 35.23 38.6647V14.9687C35.23 14.4382 35.4407 13.9295 35.8158 13.5544L44.7864 4.58383Z" fill="#FE5A4E"/>
<path d="M46.23 3.99805H46.0584C45.528 3.99805 45.0193 4.20876 44.6442 4.58383L35.8158 13.4123C35.4407 13.7873 35.23 14.296 35.23 14.8265V14.998C35.23 14.4458 35.6777 13.998 36.23 13.998H43.5027C44.4567 13.998 45.23 13.2247 45.23 12.2708V4.99805C45.23 4.44576 45.6777 3.99805 46.23 3.99805Z" fill="#FFA294"/>
<g clip-path="url(#clip5_16490_20150)">
<path d="M58.7675 31.2446C57.2023 31.1287 55.6951 30.549 54.4777 29.5055C52.1009 30.0272 49.84 30.7809 47.5791 31.7084C45.782 34.8968 44.1009 36.52 42.6516 36.52C42.3617 36.52 42.0139 36.462 41.782 36.2881C41.1443 35.9983 40.7965 35.3606 40.7965 34.7229C40.7965 34.2012 40.9125 32.7519 46.4197 30.3751C47.6951 28.0562 48.6806 25.6794 49.4922 23.1867C48.7965 21.7954 47.2893 18.3751 48.3327 16.6359C48.6806 15.9983 49.3762 15.6504 50.1298 15.7084C50.7096 15.7084 51.2893 15.9983 51.6371 16.462C52.3907 17.5055 52.3327 19.7084 51.3472 22.9548C52.2748 24.6939 53.4922 26.2591 54.9414 27.5925C56.1588 27.3606 57.3762 27.1867 58.5936 27.1867C61.3182 27.2446 61.724 28.52 61.6661 29.2736C61.6661 31.2446 59.753 31.2446 58.7675 31.2446ZM42.5356 34.8388L42.7096 34.7809C43.5211 34.491 44.1588 33.9113 44.6226 33.1577C43.753 33.5055 43.0574 34.0852 42.5356 34.8388ZM50.2458 17.4475H50.0719C50.0139 17.4475 49.898 17.4475 49.84 17.5055C49.6081 18.491 49.782 19.5345 50.1878 20.462C50.5356 19.4765 50.5356 18.433 50.2458 17.4475ZM50.6516 25.8533L50.5936 25.9693L50.5356 25.9113C50.0139 27.2446 49.4342 28.578 48.7965 29.8533L48.9125 29.7954V29.9113C50.1878 29.4475 51.5791 29.0417 52.8545 28.7519L52.7965 28.6939H52.9704C52.1009 27.8243 51.2893 26.8388 50.6516 25.8533ZM58.5356 28.9258C58.0139 28.9258 57.5501 28.9258 57.0284 29.0417C57.6081 29.3316 58.1878 29.4475 58.7675 29.5055C59.1733 29.5635 59.5791 29.5055 59.9269 29.3896C59.9269 29.2157 59.6951 28.9258 58.5356 28.9258Z" fill="white"/>
</g>
</g>
<defs>
<clipPath id="clip0_16490_20150"><rect width="26" height="26" fill="white" transform="translate(0.5 29.4121) rotate(-36.3528)"/></clipPath>
<clipPath id="clip1_16490_20150"><rect width="26" height="26" fill="white" transform="translate(79.1663 14) rotate(33.3534)"/></clipPath>
<clipPath id="clip2_16490_20150"><rect width="9.49565" height="9.49565" fill="white" transform="translate(80.5903 26.8457) rotate(33.3534)"/></clipPath>
<clipPath id="clip3_16490_20150"><rect width="36" height="36" fill="white" transform="translate(61.4141 1) rotate(26.2351)"/></clipPath>
<clipPath id="clip4_16490_20150"><rect width="36" height="36" fill="white" transform="translate(8.23047 15.7471) rotate(-20.7377)"/></clipPath>
<clipPath id="clip5_16490_20150"><rect width="20.8696" height="20.8696" fill="white" transform="translate(40.7966 15.6484)"/></clipPath>
</defs>
</svg>

          <button class="upload-file-btn" type="button" @click.stop="triggerUpload">
            <Paperclip :size="16" />
            上传文件
          </button>

          <input
            ref="fileInput"
            type="file"
            multiple
            accept=".pdf,.png,.jpg,.jpeg,.webp,.gif,.bmp,.tiff,.docx,.pptx,.xlsx"
            class="hidden-input"
            @change="handleFileSelect"
          />

          <div v-if="selectedFiles.length > 0" class="selected-files">
            <div
              v-for="(file, index) in selectedFiles"
              :key="index"
              class="selected-file"
            >
              <FileText :size="16" />
              <span>{{ file.name }}</span>
              <button class="remove-file" @click="removeFile(index)">
                <X :size="14" />
              </button>
            </div>
          </div>

          <div v-if="isLoading" class="uploading-status">
            <Loader2 :size="18" class="loading-icon" />
            <span>{{ parseProgress || '正在解析中...' }}</span>
          </div>
        </div>
      </div>

      <div v-else class="compare-container">
        <div class="left-panel">
          <div class="panel-header">
            <div class="panel-title">
              <FileImage :size="16" />
              <span>原文件</span>
            </div>
            <div v-if="previewMode === 'pdf'" class="panel-controls">
              <div class="zoom-controls">
                <button class="control-btn" @click="zoomOut">
                  <Minus :size="14" />
                </button>
                <span class="zoom-value">{{ Math.round(pdfScale * 100) }}%</span>
                <button class="control-btn" @click="zoomIn">
                  <PlusIcon :size="14" />
                </button>
              </div>
            </div>
          </div>
          <div class="panel-content preview-area" ref="previewContent">

            <div v-if="isLoadingPreview" class="preview-loading-overlay">
              <Loader2 :size="48" class="loading-icon" />
              <p>正在加载原文件...</p>
            </div>

            <div v-else-if="previewError" class="preview-error-overlay">
              <AlertCircle :size="48" class="error-icon" />
              <p>{{ previewError }}</p>
              <button v-if="previewMode === 'pdf'" class="error-action" @click="switchToMarkdown">
                <FileText :size="18" />
                查看 Markdown 内容
              </button>
            </div>

            <template v-else>
              <div v-if="previewMode === 'pdf' && pdfFallbackMode" ref="pdfPagesWrapper" class="pdf-pages-wrapper pdf-fallback-wrapper">
                <div
                  v-for="pageNum in totalPages"
                  :key="pageNum"
                  class="pdf-page-container"
                >
                  <img
                    :src="`${baseURL}/tasks/${currentTaskId}/pdf-page/${pageNum}?dpi=150`"
                    class="pdf-fallback-image"
                    :style="{ transform: `scale(${pdfScale})`, transformOrigin: 'top center' }"
                    :alt="`第 ${pageNum} 页`"
                    loading="lazy"
                  />
                </div>
              </div>

              <div v-else-if="previewMode === 'pdf'" ref="pdfPagesWrapper" class="pdf-pages-wrapper">
                <div
                  v-for="pageNum in totalPages"
                  :key="pageNum"
                  class="pdf-page-container"
                >
                  <canvas
                    :id="'pdf-canvas-' + pageNum"
                    class="pdf-canvas"
                  ></canvas>
                </div>
              </div>

              <div v-else-if="previewMode === 'image'" class="image-preview-wrapper">
                <img :src="previewSrc" class="preview-image" />
              </div>

              <div v-else-if="previewMode === 'docx'" class="office-preview-wrapper">
                <VueOfficeDocx :src="previewSrc" class="office-component" @rendered="onOfficeRendered" @error="onOfficeError" />
              </div>

              <div v-else-if="previewMode === 'excel'" class="office-preview-wrapper">
                <VueOfficeExcel :src="previewSrc" class="office-component" @rendered="onOfficeRendered" @error="onOfficeError" />
              </div>

              <div v-else-if="previewMode === 'pptx'" class="pptx-tiled-wrapper">
                <VueOfficePptx :src="previewSrc" class="pptx-tiled-component" @rendered="onOfficeRendered" @error="onOfficeError" />
              </div>
            </template>
          </div>
        </div>

        <div class="right-panel">
          <div class="panel-header">
            <div class="tab-container">
              <button
                v-for="tab in tabs"
                :key="tab.value"
                class="tab-item"
                :class="{ active: activeTab === tab.value }"
                @click="activeTab = tab.value; handleActiveTabChange(tab.value)"
              >
                {{ tab.label }}
              </button>
            </div>
            <div class="panel-header-right">
              <div v-if="activeTab === 'markdown'" class="mode-switch">
                <button
                  class="mode-btn"
                  :class="{ active: markdownMode === 'preview' }"
                  @click="markdownMode = 'preview'"
                  title="预览模式"
                >
                  <Eye :size="16" />
                </button>
                <button
                  class="mode-btn"
                  :class="{ active: markdownMode === 'edit' }"
                  @click="markdownMode = 'edit'"
                  title="编辑模式"
                >
                  <Edit3 :size="16" />
                </button>
              </div>
              <div v-if="activeTab === 'mindmap'" class="mindmap-actions-header">
                <div class="ai-summary-toggle">
                  <span class="ai-summary-label">AI 总结</span>
                  <el-switch
                    v-model="aiSummaryEnabled"
                    :loading="isSummarizing"
                    @change="handleAiSummaryToggle"
                    size="small"
                  />
                  <button
                    v-if="aiSummaryEnabled"
                    class="header-action-btn ai-refresh-btn"
                    @click="handleAiSummaryRefresh"
                    title="重新生成 AI 总结"
                  >
                    <RefreshCw :size="16" />
                  </button>
                </div>
                <span class="node-count">已生成 {{ nodeCount }} 个节点</span>
                <div class="header-actions">
                  <button class="header-action-btn" @click="downloadMindMap('svg')" title="下载 SVG">
                    <Download :size="18" />
                  </button>
                  <button class="header-action-btn" @click="resetMindMapView" title="重置视图">
                    <RotateCcw :size="18" />
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div
            class="panel-content result-content"
          >
            <div v-if="isLoading" class="loading-state">
              <Loader2 :size="48" class="loading-icon" />
              <p>正在加载解析结果...</p>
            </div>

            <div v-else-if="error" class="error-state">
              <AlertCircle :size="48" class="error-icon" />
              <p>{{ error }}</p>
              <button class="error-action" @click="selectedTask = null">
                <ArrowLeft :size="18" />
                返回上传
              </button>
            </div>

            <div v-else class="tab-content-wrapper">
              <Transition name="fade" mode="out-in">
                <div v-if="activeTab === 'markdown'" :key="`markdown-${markdownMode}`" class="markdown-wrapper">
                  <div v-if="markdownMode === 'preview'" v-html="renderedMarkdown"></div>
                  <textarea
                    v-else
                    v-model="markdown"
                    class="markdown-editor"
                    placeholder="在此编辑 Markdown..."
                    spellcheck="false"
                  ></textarea>
                </div>

                <div v-else-if="activeTab === 'mindmap'" key="mindmap" class="mindmap-view">
                  <div class="mindmap-container">
                    <div class="mindmap-content" @wheel.prevent="handleMindMapWheel">
                      <div v-if="!markdown || markdown.trim() === '' || markdown.trim() === '# 暂无解析结果'" class="empty-state">
                        <FileText :size="48" class="empty-icon" />
                        <p class="empty-text">暂无思维导图内容</p>
                        <p class="empty-subtext">请先上传并解析文档</p>
                      </div>
                      <div v-else-if="isSummarizing && aiSummaryEnabled" class="ai-loading-state">
                        <Loader2 :size="36" class="loading-icon" />
                        <p class="ai-loading-text">AI 正在总结...</p>
                      </div>
                      <div v-else-if="summaryError && aiSummaryEnabled" class="ai-error-state">
                        <AlertCircle :size="36" class="error-icon" />
                        <p class="ai-error-text">{{ summaryError }}</p>
                      </div>
                      <svg v-else ref="mindmapSvgRef" class="markmap-svg"></svg>
                    </div>
                  </div>
                </div>

                <div v-else-if="activeTab === 'json'" key="json" class="json-view">
                  <pre class="json-code">{{ formattedJson }}</pre>
                </div>
              </Transition>
            </div>
          </div>
        </div>
      </div>
    </main>

    <SettingsDrawer v-model="settingsDrawerVisible" />
  </div>
</template>

<script setup>
import { ref, computed, markRaw, onMounted, onUnmounted, watch, nextTick } from 'vue';
import {
  PlusCircle, Clock, FileText, FileImage,
  Paperclip, X, Settings, Search, Trash2,
  ArrowLeft, Copy, Download, Loader2, AlertCircle,
  Star, Plus as PlusIcon, Minus,
  CheckCircle, PanelLeftClose, PanelLeftOpen,
  Eye, Edit3, Share2, RotateCcw, RefreshCw,
  ChevronRight
} from 'lucide-vue-next';
import MarkdownIt from 'markdown-it';
import * as pdfjsLib from 'pdfjs-dist';
import { ElMessage } from 'element-plus';

import VueOfficeDocx from '@vue-office/docx';
import VueOfficeExcel from '@vue-office/excel';
import VueOfficePptx from '@vue-office/pptx';
import '@vue-office/docx/lib/index.css';
import '@vue-office/excel/lib/index.css';

import { useAiSettingsStore } from '../stores/aiSettings';
import { useAiSummarize } from '../composables/useAiSummarize';
import { useConfigStore } from '../stores/configStore';
import SettingsDrawer from '../components/SettingsDrawer.vue';

import iconPdf from '../assets/icons/document-pdf-24-filled.svg';
import iconWord from '../assets/icons/document-word-24-filled.svg';
import iconExcel from '../assets/icons/document-excel-24-filled.svg';
import iconPpt from '../assets/icons/document-powerpoint-24-filled.svg';
import iconImage from '../assets/icons/image-24-filled.svg';
import iconDoc from '../assets/icons/document-24-filled.svg';

const logoIcon = markRaw(FileText);
const fileInput = ref(null);
const isDragOver = ref(false);
const selectedFiles = ref([]);
const isLoading = ref(false);
const parseProgress = ref('');
const error = ref('');
const selectedTask = ref(null);
const isFavorite = ref(false);
const sidebarCollapsed = ref(false);
const showTaskList = ref(false);
const searchQuery = ref('');

const toggleTaskList = () => {
  showTaskList.value = !showTaskList.value;
};

const closeTaskList = () => {
  showTaskList.value = false;
};
const markdownMode = ref('preview');

const filteredTasks = computed(() => {
  if (!searchQuery.value.trim()) {
    return allTasks.value;
  }
  const query = searchQuery.value.toLowerCase();
  return allTasks.value.filter(task => {
    const name = (task.name || task.file_names?.[0] || '').toLowerCase();
    return name.includes(query);
  });
});

const configStore = useConfigStore();

const typedText = ref('');
const fullText = '让文档内容为AI所用';

const activeTab = ref('mindmap');
const tabs = [
  { label: '思维导图', value: 'mindmap' },
  { label: 'Markdown', value: 'markdown' },
  { label: 'JSON', value: 'json' },
];

const settingsDrawerVisible = ref(false);
const aiSummaryEnabled = ref(false);

const aiSettingsStore = useAiSettingsStore();
const { isSummarizing, summaryError, currentSummary, fetchSummary, clearCache, hasCachedSummary } = useAiSummarize();

const previewContent = ref(null);
const pdfPagesWrapper = ref(null);
let pdfResizeObserver = null;

const isLoadingPreview = ref(false);
const previewError = ref('');
const previewMode = ref('pdf');
const previewSrc = ref('');

const showSuccess = ref(false);
const showError = ref(false);
const successMessage = ref('');
const errorMessage = ref('');

const allTasks = ref([]);

const markdown = ref('');
const contentListJson = ref(null);
const baseURL = import.meta.env.VITE_MINERU_API_URL || 'http://localhost:8000';

let rawPdfDoc = null;
const totalPages = ref(1);
const pdfScale = ref(1);
const pdfFallbackMode = ref(false);
const currentTaskId = ref('');

const resolvedParseDir = ref('');
const mindmapSvgRef = ref(null);
let mmInstance = null;
const mindmapScale = ref(1);
let transformer = null;

const parseDirCandidates = ['auto', 'office', 'vlm', 'hybrid_auto', 'txt', 'ocr', 'hybrid_txt', 'hybrid_ocr'];

const imageExts = ['jpg', 'jpeg', 'png', 'webp', 'gif', 'bmp', 'tiff', 'svg'];
const officeDocExts = ['docx', 'doc'];
const officeExcelExts = ['xlsx', 'xls'];
const officePptxExts = ['pptx', 'ppt'];
const allKnownExts = ['pdf', ...imageExts, ...officeDocExts, ...officeExcelExts, ...officePptxExts];

const getFileTypes = computed(() => {
  const types = { pdf: false, doc: false, xls: false, ppt: false, image: false };
  selectedFiles.value.forEach(file => {
    const ext = file.name.toLowerCase().substring(file.name.lastIndexOf('.'));
    if (ext === '.pdf') types.pdf = true;
    else if (ext === '.doc' || ext === '.docx') types.doc = true;
    else if (ext === '.xls' || ext === '.xlsx') types.xls = true;
    else if (ext === '.ppt' || ext === '.pptx') types.ppt = true;
    else if (['.png', '.jpg', '.jpeg', '.webp', '.gif', '.bmp', '.tiff'].includes(ext)) types.image = true;
  });
  return types;
});

const getFileIcon = (fileName) => {
  if (!fileName) return iconDoc;
  const ext = fileName.split('.').pop().toLowerCase();
  if (ext === 'pdf') return iconPdf;
  if (officeDocExts.includes(ext)) return iconWord;
  if (officeExcelExts.includes(ext)) return iconExcel;
  if (officePptxExts.includes(ext)) return iconPpt;
  if (imageExts.includes(ext)) return iconImage;
  return iconDoc;
};

const getPreviewMode = (fileName) => {
  if (!fileName) return 'pdf';
  const ext = fileName.toLowerCase().split('.').pop();
  if (ext === 'pdf') return 'pdf';
  if (imageExts.includes(ext)) return 'image';
  if (officeDocExts.includes(ext)) return 'docx';
  if (officeExcelExts.includes(ext)) return 'excel';
  if (officePptxExts.includes(ext)) return 'pptx';
  return 'pdf';
};

const getUploadFileUrl = (task) => {
  if (!task?.task_id || !task.file_names?.[0]) return '';
  const encodedFileName = encodeURIComponent(task.file_names[0]);
  return `${baseURL}/static/output/${task.task_id}/uploads/${encodedFileName}`;
};

const resolveParseDir = async (task) => {
  if (!task?.task_id || !task.file_names?.[0]) return '';
  const baseName = task.file_names[0].replace(/\.[^/.]+$/, '');
  const encodedBaseName = encodeURIComponent(baseName);
  for (const dir of parseDirCandidates) {
    const mdUrl = `${baseURL}/static/output/${task.task_id}/${encodedBaseName}/${dir}/${encodedBaseName}.md`;
    try {
      const resp = await fetch(mdUrl, { method: 'HEAD' });
      if (resp.ok) return dir;
    } catch (_) {}
  }
  return '';
};

const fixImagePaths = (mdContent, taskId) => {
  if (!mdContent || !taskId) return mdContent;
  const imageRegex = /!\[([^\]]*)\]\((images\/[^)]+)\)/g;
  const fileName = selectedTask.value?.file_names?.[0] || 'document';
  const outputDir = resolvedParseDir.value || 'auto';
  const encodedFileName = encodeURIComponent(fileName.replace(/\.[^/.]+$/, ''));
  return mdContent.replace(imageRegex, (match, altText, relativePath) => {
    const fullUrl = `${baseURL}/static/output/${taskId}/${encodedFileName}/${outputDir}/${relativePath}`;
    return `![${altText}](${fullUrl})`;
  });
};

const md = new MarkdownIt({ html: true, linkify: true, typographer: true });

const renderedMarkdown = computed(() => {
  const fixedContent = fixImagePaths(markdown.value, selectedTask.value?.task_id);
  return md.render(fixedContent);
});

const formattedJson = computed(() => {
  if (contentListJson.value) {
    return JSON.stringify(contentListJson.value, null, 2);
  }
  const jsonData = {
    task_id: selectedTask.value?.task_id || '',
    file_names: selectedTask.value?.file_names || [],
    status: selectedTask.value?.status || '',
    content_length: markdown.value.length,
  };
  return JSON.stringify(jsonData, null, 2);
});

const nodeCount = computed(() => {
  const content = aiSummaryEnabled.value && currentSummary.value
    ? currentSummary.value
    : markdown.value;
  if (!content) return 0;
  return (content.match(/^#{1,6}\s+/gm) || []).length;
});

const destroyMarkmap = () => {
  if (mmInstance) {
    try {
      if (typeof mmInstance.destroy === 'function') {
        mmInstance.destroy();
      }
    } catch (_) {}
    mmInstance = null;
  }
};

const initMarkmap = async () => {
  const content = aiSummaryEnabled.value && currentSummary.value
    ? currentSummary.value
    : markdown.value;

  if (!content || content.trim() === '' || content.trim() === '# 暂无解析结果') {
    return;
  }

  await nextTick();

  if (!mindmapSvgRef.value) {
    setTimeout(initMarkmap, 50);
    return;
  }

  try {
    const markmap = window.markmap;
    if (!markmap) return;

    if (!transformer) {
      transformer = new markmap.Transformer();
    }

    const { root } = transformer.transform(content);
    const { styles, scripts } = transformer.getAssets();

    if (styles && markmap.loadCSS) markmap.loadCSS(styles);
    if (scripts && markmap.loadJS) markmap.loadJS(scripts);

    await nextTick();

    const svgEl = mindmapSvgRef.value;
    const container = svgEl.parentElement;
    if (container) {
      const rect = container.getBoundingClientRect();
      if (rect.width > 0 && rect.height > 0) {
        svgEl.setAttribute('width', rect.width.toString());
        svgEl.setAttribute('height', rect.height.toString());
        svgEl.style.width = rect.width + 'px';
        svgEl.style.height = rect.height + 'px';
      }
    }

    destroyMarkmap();

    mmInstance = markmap.Markmap.create(svgEl, {
      autoFit: true,
      fitRatio: 0.95,
      initialExpandLevel: -1
    }, root);
    
    // 确保渲染后再次适配
    await nextTick();
    setTimeout(() => {
      if (mmInstance) {
        mmInstance.fit();
      }
    }, 100);
  } catch (error) {
    console.error('Error initializing markmap:', error);
    mmInstance = null;
  }
};

const downloadMindMap = (format = 'svg') => {
  if (!mindmapSvgRef.value) return;

  if (mmInstance) {
    mmInstance.fit();
  }

  if (format === 'svg') {
    const svg = mindmapSvgRef.value;
    const svgCopy = svg.cloneNode(true);
    
    if (!svgCopy.getAttribute('xmlns')) {
      svgCopy.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
    }
    
    const boundingRect = svg.getBoundingClientRect();
    svgCopy.setAttribute('width', boundingRect.width.toString());
    svgCopy.setAttribute('height', boundingRect.height.toString());
    
    const svgData = new XMLSerializer().serializeToString(svgCopy);
    const blob = new Blob([svgData], { type: 'image/svg+xml' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `mindmap_${new Date().getTime()}.svg`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }
};

const resetMindMapView = () => {
  mmInstance?.fit();
  mindmapScale.value = 1;
};

const handleMindMapWheel = (event) => {
  event.preventDefault();
  const delta = event.deltaY > 0 ? -0.1 : 0.1;
  if ((mindmapScale.value > 0.5 || delta > 0) && (mindmapScale.value < 2 || delta < 0)) {
    mindmapScale.value += delta;
    if (mmInstance && typeof mmInstance.setScale === 'function') {
      mmInstance.setScale(mindmapScale.value);
    }
  }
};

const handleMindMapResize = () => {
  mmInstance?.fit();
};

const handleActiveTabChange = async (newTab) => {
  if (newTab === 'mindmap') {
    await nextTick();
    await nextTick();
    if (aiSummaryEnabled.value && currentSummary.value) {
      await renderMindmapFromContent(currentSummary.value);
    } else {
      initMarkmap();
    }
  } else {
    destroyMarkmap();
  }
};

const watchMarkdown = async () => {
  if (activeTab.value === 'mindmap') {
    await nextTick();
    if (aiSummaryEnabled.value && currentSummary.value) {
      await renderMindmapFromContent(currentSummary.value);
    } else {
      initMarkmap();
    }
  }
};

const probeUploadFileName = async (baseName, taskId) => {
  for (const ext of allKnownExts) {
    const candidate = `${baseName}.${ext}`;
    const testUrl = `${baseURL}/static/output/${taskId}/uploads/${encodeURIComponent(candidate)}`;
    try {
      const resp = await fetch(testUrl, { method: 'HEAD' });
      if (resp.ok) return candidate;
    } catch (_) {}
  }
  return baseName;
};

const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

const getPdfContainerWidth = () => {
  const wrapper = pdfPagesWrapper.value;
  if (wrapper) {
    const style = getComputedStyle(wrapper);
    const paddingX = parseFloat(style.paddingLeft || 0) + parseFloat(style.paddingRight || 0);
    return Math.max(0, wrapper.clientWidth - paddingX);
  }
  return Math.max(0, (previewContent.value?.clientWidth || 0) - 40);
};

const waitForPdfCanvases = async (pageCount, maxRetries = 50) => {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    await nextTick();
    const containerWidth = getPdfContainerWidth();
    const allCanvasesReady = pageCount > 0
      && Array.from({ length: pageCount }, (_, i) => document.getElementById(`pdf-canvas-${i + 1}`))
        .every(Boolean);
    if (containerWidth > 0 && allCanvasesReady) {
      return containerWidth;
    }
    await delay(100);
  }
  return getPdfContainerWidth();
};

const isCanvasBlank = (canvas) => {
  const ctx = canvas.getContext('2d');
  const w = canvas.width;
  const h = canvas.height;
  if (w === 0 || h === 0) return true;
  const sampleSize = 50;
  const stepX = Math.max(1, Math.floor(w / sampleSize));
  const stepY = Math.max(1, Math.floor(h / sampleSize));
  let nonWhitePixels = 0;
  const imageData = ctx.getImageData(0, 0, w, h);
  const data = imageData.data;
  for (let y = 0; y < h; y += stepY) {
    for (let x = 0; x < w; x += stepX) {
      const idx = (y * w + x) * 4;
      const r = data[idx];
      const g = data[idx + 1];
      const b = data[idx + 2];
      if (r < 250 || g < 250 || b < 250) {
        nonWhitePixels++;
        if (nonWhitePixels > 5) return false;
      }
    }
  }
  return true;
};

const loadFallbackPdfPages = async () => {
  if (!currentTaskId.value) return;
  pdfFallbackMode.value = true;
  if (!rawPdfDoc) {
    try {
      const resp = await fetch(`${baseURL}/tasks/${currentTaskId.value}/pdf-page/0`);
      if (resp.ok) {
        const info = await resp.json();
        totalPages.value = info.page_count || 1;
        console.log(`[PDF] 降级模式：从服务端获取页数 ${totalPages.value}`);
      }
    } catch (err) {
      console.warn('[PDF] 降级模式：获取页数失败，默认1页', err);
      totalPages.value = 1;
    }
  }
  await nextTick();
};

const renderAllPages = async () => {
  if (!rawPdfDoc || !previewContent.value || pdfFallbackMode.value) return;

  await nextTick();
  
  const wrapper = pdfPagesWrapper.value;
  if (!wrapper) return;
  
  const containerWidth = wrapper.clientWidth - 40;
  if (containerWidth <= 0) return;

  const MAX_CANVAS_DIM = 4096;
  let blankPageCount = 0;

  for (let pageNum = 1; pageNum <= rawPdfDoc.numPages; pageNum++) {
    try {
      const page = await rawPdfDoc.getPage(pageNum);
      
      const viewport = page.getViewport({ scale: 1 });
      let scale = (containerWidth / viewport.width) * pdfScale.value;
      const outputScale = window.devicePixelRatio || 1;

      const rawW = Math.floor(viewport.width * scale * outputScale);
      const rawH = Math.floor(viewport.height * scale * outputScale);
      if (rawW > MAX_CANVAS_DIM || rawH > MAX_CANVAS_DIM) {
        const clampScale = MAX_CANVAS_DIM / Math.max(rawW, rawH);
        scale *= clampScale;
      }

      const scaledViewport = page.getViewport({ scale });

      const pdfCanvasEl = document.getElementById('pdf-canvas-' + pageNum);
      if (!pdfCanvasEl) continue;

      const canvasW = Math.floor(scaledViewport.width * outputScale);
      const canvasH = Math.floor(scaledViewport.height * outputScale);
      pdfCanvasEl.width = canvasW;
      pdfCanvasEl.height = canvasH;
      pdfCanvasEl.style.width = Math.floor(scaledViewport.width) + 'px';
      pdfCanvasEl.style.height = Math.floor(scaledViewport.height) + 'px';

      const ctx = pdfCanvasEl.getContext('2d');

      ctx.scale(outputScale, outputScale);
      ctx.fillStyle = '#ffffff';
      ctx.fillRect(0, 0, scaledViewport.width, scaledViewport.height);

      const renderTask = page.render({
        canvasContext: ctx,
        viewport: scaledViewport,
        intent: 'display',
        enableWebGL: false,
      });

      await renderTask.promise;

      if (isCanvasBlank(pdfCanvasEl)) {
        blankPageCount++;
        console.warn(`PDF 第 ${pageNum} 页渲染结果为空白（可能是 OCR 扫描件 1-bit 图像兼容问题）`);
      }
    } catch (pageErr) {
      console.warn(`PDF 第 ${pageNum} 页渲染失败:`, pageErr);
      const pdfCanvasEl = document.getElementById('pdf-canvas-' + pageNum);
      if (pdfCanvasEl) {
        const ctx = pdfCanvasEl.getContext('2d');
        ctx.fillStyle = '#f9fafb';
        ctx.fillRect(0, 0, pdfCanvasEl.width, pdfCanvasEl.height);
        ctx.fillStyle = '#9ca3af';
        ctx.font = '14px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(`第 ${pageNum} 页渲染失败`, pdfCanvasEl.width / 2, pdfCanvasEl.height / 2);
      }
      blankPageCount++;
    }
  }

  if (blankPageCount > 0 && blankPageCount >= rawPdfDoc.numPages * 0.5 && currentTaskId.value) {
    console.warn(`PDF 渲染空白页过多 (${blankPageCount}/${rawPdfDoc.numPages})，切换到服务端渲染降级模式`);
    await loadFallbackPdfPages();
  }
};

const setupPdfResizeObserver = () => {
  pdfResizeObserver?.disconnect();
  const target = pdfPagesWrapper.value || previewContent.value;
  if (!target) return;
  pdfResizeObserver = new ResizeObserver(() => {
    if (rawPdfDoc && previewMode.value === 'pdf' && !isLoadingPreview.value && !pdfFallbackMode.value) {
      renderAllPages();
    }
  });
  pdfResizeObserver.observe(target);
};

const loadContentList = async (task) => {
  contentListJson.value = null;
  if (!task?.task_id) return;

  const fileName = task.file_names?.[0] || '';
  const baseName = fileName.replace(/\.[^/.]+$/, '');
  const encodedBaseName = encodeURIComponent(baseName);
  const parseDir = resolvedParseDir.value || 'auto';

  const jsonUrl = `${baseURL}/static/output/${task.task_id}/${encodedBaseName}/${parseDir}/${encodedBaseName}_content_list_v2.json`;
  try {
    const response = await fetch(jsonUrl);
    if (response.ok) {
      contentListJson.value = await response.json();
    }
  } catch (err) {
    console.error('加载 content_list_v2.json 失败:', err);
  }
};

const loadPreview = async (task) => {
  if (!task?.task_id) return;

  const fileName = task.file_names?.[0] || '';
  previewMode.value = getPreviewMode(fileName);
  isLoadingPreview.value = true;
  previewError.value = '';
  rawPdfDoc = null;
  previewSrc.value = '';
  pdfFallbackMode.value = false;
  currentTaskId.value = task.task_id;
  if (previewMode.value === 'pdf') {
    pdfScale.value = 1;
  }

  try {
    if (previewMode.value === 'pdf') {
      await loadPdfPreview(task);
    } else {
      previewSrc.value = getUploadFileUrl(task);
    }
  } catch (err) {
    console.error('加载预览失败:', err);
    previewError.value = '加载预览失败: ' + err.message;
    isLoadingPreview.value = false;
  } finally {
    if (previewMode.value !== 'pdf') {
      isLoadingPreview.value = false;
    }
  }
};

const loadPdfPreview = async (task) => {
  let targetUrl = '';
  const baseName = (task.file_names?.[0] || '').replace(/\.[^/.]+$/, '');
  const encodedBaseName = encodeURIComponent(baseName);
  const encodedFileName = encodeURIComponent(task.file_names?.[0] || '');

  if (task.pdf_path) {
    const relativePath = task.pdf_path.replace(/^.*output\//, '');
    targetUrl = `${baseURL}/static/output/${relativePath}`;
  }

  if (!targetUrl && baseName && resolvedParseDir.value) {
    const originUrl = `${baseURL}/static/output/${task.task_id}/${encodedBaseName}/${resolvedParseDir.value}/${encodedBaseName}_origin.pdf`;
    try {
      const resp = await fetch(originUrl, { method: 'HEAD' });
      if (resp.ok) targetUrl = originUrl;
    } catch (_) {}
  }

  if (!targetUrl && baseName) {
    const pdfCandidates = parseDirCandidates.map(
      dir => `${baseURL}/static/output/${task.task_id}/${encodedBaseName}/${dir}/${encodedBaseName}_origin.pdf`
    );
    pdfCandidates.push(`${baseURL}/static/output/${task.task_id}/uploads/${encodedFileName}`);

    const probedFileName = await probeUploadFileName(baseName, task.task_id);
    if (probedFileName !== baseName) {
      pdfCandidates.push(
        `${baseURL}/static/output/${task.task_id}/uploads/${encodeURIComponent(probedFileName)}`
      );
    }

    for (const url of pdfCandidates) {
      try {
        const resp = await fetch(url, { method: 'HEAD' });
        if (resp.ok) {
          targetUrl = url;
          break;
        }
      } catch (_) {}
    }
  }

  if (!targetUrl) {
    previewError.value = '无法找到PDF文件';
    isLoadingPreview.value = false;
    return;
  }

  pdfjsLib.GlobalWorkerOptions.workerSrc = '/pdfjs/pdf.worker.min.mjs';

  const pdfLoadConfig = {
    enableXfa: false,
    disableFontFace: false,
    useSystemFonts: true,
    isEvalSupported: true,
    useWorkerFetch: false,
    ignoreErrors: true,
  };

  let doc;
  try {
    console.log(`[PDF] 开始加载: ${targetUrl}`);
    const response = await fetch(targetUrl);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const pdfData = await response.arrayBuffer();
    console.log(`[PDF] ArrayBuffer 大小: ${(pdfData.byteLength / 1024).toFixed(1)} KB`);
    const loadingTask = pdfjsLib.getDocument({
      data: pdfData,
      ...pdfLoadConfig,
    });
    doc = await loadingTask.promise;
    console.log(`[PDF] 加载成功，共 ${doc.numPages} 页`);
  } catch (fetchErr) {
    console.warn('[PDF] ArrayBuffer 加载失败，回退 URL 加载:', fetchErr);
    try {
      const loadingTask = pdfjsLib.getDocument({
        url: targetUrl,
        ...pdfLoadConfig,
      });
      doc = await loadingTask.promise;
      console.log(`[PDF] URL 加载成功，共 ${doc.numPages} 页`);
    } catch (urlErr) {
      console.error('[PDF] URL 加载也失败:', urlErr);
      if (currentTaskId.value) {
        console.warn('[PDF] 尝试服务端渲染降级模式');
        totalPages.value = 1;
        await loadFallbackPdfPages();
        isLoadingPreview.value = false;
        return;
      }
      previewError.value = 'PDF 文件加载失败，该文件可能不受支持';
      isLoadingPreview.value = false;
      return;
    }
  }

  rawPdfDoc = doc;
  totalPages.value = doc.numPages;

  isLoadingPreview.value = false;
  await nextTick();

  try {
    console.log(`[PDF] 开始渲染 ${doc.numPages} 页，容器宽度: ${pdfPagesWrapper.value?.clientWidth || 'unknown'}`);
    await renderAllPages();
    if (pdfFallbackMode.value) {
      console.log('[PDF] 已切换到服务端渲染降级模式');
      isLoadingPreview.value = false;
      return;
    }
    setupPdfResizeObserver();
    await delay(200);
    await renderAllPages();
    if (pdfFallbackMode.value) {
      console.log('[PDF] 二次渲染后切换到服务端渲染降级模式');
      isLoadingPreview.value = false;
      return;
    }
    console.log('[PDF] 渲染完成');
  } catch (renderErr) {
    console.error('[PDF] 渲染失败:', renderErr);
    if (currentTaskId.value && !pdfFallbackMode.value) {
      console.warn('[PDF] 渲染异常，尝试服务端渲染降级模式');
      await loadFallbackPdfPages();
      isLoadingPreview.value = false;
      return;
    }
    previewError.value = 'PDF 渲染失败，请尝试查看解析后的 Markdown 内容';
    isLoadingPreview.value = false;
  }
};

const onOfficeRendered = () => {
  isLoadingPreview.value = false;
};

const onOfficeError = (err) => {
  console.error('Office预览渲染失败:', err);
  previewError.value = 'Office文件预览失败';
  isLoadingPreview.value = false;
};

const switchToMarkdown = () => {
  previewError.value = '';
  activeTab.value = 'markdown';
  markdownMode.value = 'preview';
};

const zoomIn = () => {
  if (pdfScale.value < 3) {
    pdfScale.value += 0.25;
    renderAllPages();
  }
};

const zoomOut = () => {
  if (pdfScale.value > 0.5) {
    pdfScale.value -= 0.25;
    renderAllPages();
  }
};

const validExtensions = ['.pdf', '.png', '.jpg', '.jpeg', '.webp', '.gif', '.bmp', '.tiff', '.docx', '.pptx', '.xlsx'];

const addFiles = (newFiles) => {
  const prevCount = selectedFiles.value.length;
  newFiles.forEach((file) => {
    const ext = file.name.toLowerCase().substring(file.name.lastIndexOf('.'));
    if (!validExtensions.includes(ext)) return;
    if (!selectedFiles.value.some((f) => f.name === file.name && f.size === file.size)) {
      selectedFiles.value.push(file);
    }
  });
  if (selectedFiles.value.length > prevCount && !isLoading.value) {
    startParse();
  }
};

const onDragOver = () => {
  isDragOver.value = true;
};

const onDragLeave = (event) => {
  if (!event.currentTarget.contains(event.relatedTarget)) {
    isDragOver.value = false;
  }
};

const handleDrop = (event) => {
  isDragOver.value = false;
  const files = Array.from(event.dataTransfer.files);
  addFiles(files);
};

const triggerUpload = () => {
  fileInput.value?.click();
};

const handleFileSelect = (event) => {
  const files = Array.from(event.target.files);
  addFiles(files);
  event.target.value = '';
};

const removeFile = (index) => {
  selectedFiles.value.splice(index, 1);
};

const selectTask = (task, localMarkdown = null) => {
  aiSummaryEnabled.value = false;
  currentSummary.value = '';
  summaryError.value = '';
  selectedTask.value = task;
  loadTaskResult(task, localMarkdown);
};

const loadTaskResult = async (task, localMarkdown = null) => {
  isLoading.value = true;
  error.value = '';

  try {
    resolvedParseDir.value = await resolveParseDir(task);

    if (localMarkdown) {
      markdown.value = localMarkdown;
      await nextTick();
      await loadPreview(task);
      return;
    }

    let mdLoaded = false;

    const response = await fetch(`${baseURL}/tasks/${task.task_id}/result`);
    if (response.ok) {
      const data = await response.json();

      if (data.results) {
        const resultKeys = Object.keys(data.results);

        if (resultKeys.length > 0) {
          const firstFileResult = data.results[resultKeys[0]];

          if (firstFileResult.md_content) {
            markdown.value = firstFileResult.md_content;
            mdLoaded = true;
          }
        }
      }
    }

    if (!mdLoaded) {
      const fileName = task.file_names?.[0] || '';
      const baseName = fileName.replace(/\.[^/.]+$/, '');
      const encodedBaseName = encodeURIComponent(baseName);

      if (resolvedParseDir.value) {
        const mdUrl = `${baseURL}/static/output/${task.task_id}/${encodedBaseName}/${resolvedParseDir.value}/${encodedBaseName}.md`;
        const mdResponse = await fetch(mdUrl);
        if (mdResponse.ok) {
          markdown.value = await mdResponse.text();
          mdLoaded = true;
        }
      }

      if (!mdLoaded) {
        for (const dir of parseDirCandidates) {
          const mdUrl = `${baseURL}/static/output/${task.task_id}/${encodedBaseName}/${dir}/${encodedBaseName}.md`;
          try {
            const mdResponse = await fetch(mdUrl);
            if (mdResponse.ok) {
              markdown.value = await mdResponse.text();
              resolvedParseDir.value = dir;
              mdLoaded = true;
              break;
            }
          } catch (_) {}
        }
      }
    }

    if (!mdLoaded) {
      markdown.value = '# 暂无解析结果';
    }

    await loadContentList(task);

    await nextTick();
    await loadPreview(task);
  } catch (err) {
    console.error('加载任务失败:', err);
    error.value = '加载任务失败，请稍后重试';
    markdown.value = '# 加载失败';
  } finally {
    isLoading.value = false;
  }
};

const loadTaskList = async () => {
  try {
    const response = await fetch(`${baseURL}/api/list-output-files`);
    if (!response.ok) {
      throw new Error('获取任务列表失败');
    }
    const data = await response.json();
    if (data && Array.isArray(data.files)) {
      const tasks = [];
      for (const item of data.files) {
        const baseName = item.name || 'unknown';
        const actualFileName = await probeUploadFileName(baseName, item.task_id);
        tasks.push({
          task_id: item.task_id,
          file_names: [actualFileName],
          name: item.name,
          status: item.status,
          pdf_path: item.pdfPath
        });
      }
      allTasks.value = tasks;
    }
  } catch (err) {
    console.error('加载任务列表失败:', err);
  }
};

const handleDeleteTask = async (task) => {
  if (!task?.task_id) return;
  
  try {
    const response = await fetch(`${baseURL}/tasks/${task.task_id}`, {
      method: 'DELETE'
    });
    
    if (response.ok) {
      allTasks.value = allTasks.value.filter(t => t.task_id !== task.task_id);
      
      if (selectedTask.value?.task_id === task.task_id) {
        selectedTask.value = null;
      }
      
      ElMessage.success('删除成功');
    } else {
      throw new Error('删除失败');
    }
  } catch (err) {
    console.error('删除任务失败:', err);
    ElMessage.error('删除失败，请稍后重试');
  }
};

const startParse = async () => {
  if (selectedFiles.value.length === 0) {
    errorMessage.value = '请先选择文件';
    showError.value = true;
    return;
  }

  isLoading.value = true;
  parseProgress.value = '提交解析任务...';

  try {
    const formData = new FormData();
    selectedFiles.value.forEach(file => {
      formData.append('files', file);
    });
    const opts = configStore.requestOptions;
    formData.append('backend', opts.backend);
    formData.append('parse_method', opts.parse_method);
    formData.append('lang_list', opts.lang_list);
    formData.append('start_page_id', opts.start_page_id);
    if (opts.end_page_id) formData.append('end_page_id', opts.end_page_id);
    formData.append('formula_enable', opts.formula_enable);
    formData.append('table_enable', opts.table_enable);
    formData.append('image_analysis', opts.image_analysis);
    formData.append('return_content_list', 'true');

    const submitResponse = await fetch(`${baseURL}/tasks`, {
      method: 'POST',
      body: formData,
    });

    if (!submitResponse.ok) {
      throw new Error('提交任务失败');
    }

    const submitData = await submitResponse.json();
    const taskId = submitData.task_id;
    parseProgress.value = '任务已提交，等待解析...';

    let completed = false;
    while (!completed) {
      await new Promise(resolve => setTimeout(resolve, 2000));

      const statusResponse = await fetch(`${baseURL}/tasks/${taskId}`);
      if (!statusResponse.ok) {
        throw new Error('获取任务状态失败');
      }

      const statusData = await statusResponse.json();
      parseProgress.value = `解析中... 状态: ${statusData.status}`;

      if (statusData.status === 'completed') {
        completed = true;

        const resultResponse = await fetch(`${baseURL}/tasks/${taskId}/result`);
        if (resultResponse.ok) {
          const resultData = await resultResponse.json();

          if (resultData.results) {
            const resultKeys = Object.keys(resultData.results);
            if (resultKeys.length > 0) {
              const firstFileResult = resultData.results[resultKeys[0]];

              if (firstFileResult.md_content) {
                markdown.value = firstFileResult.md_content;
              }
            }
          }
        }

        const newTask = {
          task_id: taskId,
          file_names: selectedFiles.value.map(f => f.name),
          status: 'completed',
        };
        allTasks.value.unshift(newTask);

        selectedTask.value = newTask;
        resolvedParseDir.value = await resolveParseDir(newTask);
        await nextTick();
        await loadPreview(newTask);

        successMessage.value = '解析完成';
        showSuccess.value = true;
      } else if (statusData.status === 'failed') {
        throw new Error(statusData.error || '解析失败');
      }
    }
  } catch (err) {
    errorMessage.value = err.message || '提交任务失败';
    showError.value = true;
  } finally {
    isLoading.value = false;
    parseProgress.value = '';
  }
};

const handleNewParse = () => {
  selectedFiles.value = [];
  isLoading.value = false;
  selectedTask.value = null;
  parseProgress.value = '';
  showError.value = false;
  aiSummaryEnabled.value = false;
};

const toggleFavorite = () => {
  isFavorite.value = !isFavorite.value;
  successMessage.value = isFavorite.value ? '已添加到收藏' : '已取消收藏';
  showSuccess.value = true;
};


const handleAiSummaryToggle = async (enabled) => {
  if (enabled) {
    if (!aiSettingsStore.isConfigured) {
      ElMessage.warning('请先在侧边栏配置 AI 模型设置');
      aiSummaryEnabled.value = false;
      settingsDrawerVisible.value = true;
      return;
    }
    if (!markdown.value || markdown.value.trim() === '' || markdown.value.trim() === '# 暂无解析结果') {
      ElMessage.warning('暂无内容可供总结');
      aiSummaryEnabled.value = false;
      return;
    }
    const taskId = selectedTask.value?.task_id;
    if (!taskId) {
      aiSummaryEnabled.value = false;
      return;
    }
    if (!hasCachedSummary(taskId)) {
      await fetchSummary(taskId, markdown.value);
    } else {
      currentSummary.value = (await fetchSummary(taskId, markdown.value));
    }
    if (currentSummary.value) {
      await renderMindmapFromContent(currentSummary.value);
    }
  } else {
    await renderMindmapFromContent(markdown.value);
  }
};

const handleAiSummaryRefresh = async () => {
  const taskId = selectedTask.value?.task_id;
  if (!taskId || !markdown.value) return;
  clearCache(taskId);
  await fetchSummary(taskId, markdown.value);
  if (currentSummary.value) {
    await renderMindmapFromContent(currentSummary.value);
  }
};

const renderMindmapFromContent = async (content) => {
  if (!content || content.trim() === '') return;
  await nextTick();
  if (!mindmapSvgRef.value) {
    setTimeout(() => renderMindmapFromContent(content), 50);
    return;
  }
  try {
    const markmap = window.markmap;
    if (!markmap) return;
    if (!transformer) {
      transformer = new markmap.Transformer();
    }
    const { root } = transformer.transform(content);
    const { styles, scripts } = transformer.getAssets();
    if (styles && markmap.loadCSS) markmap.loadCSS(styles);
    if (scripts && markmap.loadJS) markmap.loadJS(scripts);
    await nextTick();
    const svgEl = mindmapSvgRef.value;
    const container = svgEl.parentElement;
    if (container) {
      const rect = container.getBoundingClientRect();
      if (rect.width > 0 && rect.height > 0) {
        svgEl.setAttribute('width', rect.width.toString());
        svgEl.setAttribute('height', rect.height.toString());
        svgEl.style.width = rect.width + 'px';
        svgEl.style.height = rect.height + 'px';
      }
    }
    destroyMarkmap();
    mmInstance = markmap.Markmap.create(svgEl, {
      autoFit: true,
      fitRatio: 0.95,
      initialExpandLevel: -1
    }, root);
    await nextTick();
    setTimeout(() => {
      if (mmInstance) mmInstance.fit();
    }, 100);
  } catch (err) {
    console.error('渲染思维导图失败:', err);
  }
};

const copyContent = async () => {
  try {
    await navigator.clipboard.writeText(markdown.value);
    successMessage.value = '复制成功';
    showSuccess.value = true;
  } catch (err) {
    errorMessage.value = '复制失败';
    showError.value = true;
  }
};

const shareContent = () => {
  if (navigator.share) {
    navigator.share({
      title: selectedTask.value?.name || 'Document',
      text: 'Check out this document',
    });
  } else {
    successMessage.value = '分享功能不可用';
    showSuccess.value = true;
  }
};

const downloadMd = () => {
  const blob = new Blob([markdown.value], { type: 'text/markdown' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `${selectedTask.value?.file_names?.[0] || 'document'}.md`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);

  successMessage.value = '下载成功';
  showSuccess.value = true;
};

onMounted(() => {
  loadTaskList();
  aiSettingsStore.loadFromServer();
  window.addEventListener('resize', handleMindMapResize);
  
  let index = 0;
  const typeInterval = setInterval(() => {
    if (index < fullText.length) {
      typedText.value += fullText[index];
      index++;
    } else {
      clearInterval(typeInterval);
    }
  }, 150);
});

onUnmounted(() => {
  window.removeEventListener('resize', handleMindMapResize);
  pdfResizeObserver?.disconnect();
  destroyMarkmap();
});

watch(markdown, () => {
  watchMarkdown();
});
</script>

<style scoped>
.app-container {
  display: flex;
  height: 100vh;
  max-height: 100vh;
  background-color: #f5f5f7;
  overflow: hidden;
}

.sidebar {
  width: 260px;
  background: #F4F4F5;
  color: #374151;
  display: flex;
  flex-direction: column;
  padding: 0 16px;
  flex-shrink: 0;
  transition: width 0.25s ease, padding 0.25s ease;
  border-right: 1px solid #e5e7eb;
}

.sidebar.collapsed {
  width: 88px;
  padding: 16px 4px;
}

.sidebar-footer {
  margin-top: auto;
  padding-top: 12px;
  border-top: 1px solid #e5e7eb;
}

.sidebar.collapsed .sidebar-footer {
  padding-top: 8px;
}

.settings-btn {
  color: #6b7280 !important;
}

.settings-btn:hover {
  color: #374151 !important;
}

.sidebar-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 48px;
  padding: 0;
  border-bottom: 1px solid #e5e7eb;
}

.logo {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  gap: 10px;
  font-size: 16px;
  font-weight: 600;
  width: 100%;
  color: #374151;
  overflow: hidden;
  white-space: nowrap;
}

.sidebar.collapsed .logo {
  justify-content: center;
}

.sidebar.collapsed .sidebar-header {
  justify-content: center;
  gap: 0;
}

.logo svg {
  color: #0288d1;
  flex-shrink: 0;
}

.collapse-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border: none;
  border-radius: 6px;
  background: transparent;
  color: #9ca3af;
  cursor: pointer;
  transition: all 0.2s;
  flex-shrink: 0;
}

.collapse-btn:hover {
  background: #e5e7eb;
  color: #374151;
}

.sidebar.collapsed .collapse-btn {
  margin: 0;
}

.sidebar-nav {
  padding: 12px 0;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 10px;
  width: 100%;
  padding: 10px 12px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: #6b7280;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s;
  margin-bottom: 2px;
  white-space: nowrap;
  overflow: hidden;
}

.sidebar.collapsed .nav-item {
  justify-content: center;
  padding: 10px;
}

.nav-item:hover {
  background: #e5e7eb;
  color: #374151;
}

.nav-item.active {
  background: #0288d1;
  color: #fff;
}

.nav-item.active svg {
  color: #fff;
}

.sidebar-divider {
  height: 1px;
  background: #e5e7eb;
  margin: 8px 0;
}

.task-list {
  flex: 1;
  overflow-y: auto;
  position: relative;
}

.task-list-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 6px;
  padding: 10px 12px;
  font-size: 11px;
  color: #9ca3af;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  cursor: pointer;
}

.task-search {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 4px 8px;
  background: #fff;
  border: 1px solid #e5e7eb;
  border-radius: 6px;
  color: #9ca3af;
  font-size: 12px;
  min-width: 0;
}

.search-input {
  border: none;
  outline: none;
  background: transparent;
  font-size: 12px;
  color: #374151;
  width: 100%;
  min-width: 80px;
}

.search-input::placeholder {
  color: #9ca3af;
}

.task-list.collapsed .task-list-header {
  display: none;
}

.expand-icon {
  transition: transform 0.2s;
}

.task-list-content {
  overflow-y: auto;
}

.task-list-content.collapsed {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  gap: 2px;
  padding: 4px 0;
}

.task-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.15s;
}

.task-item:hover {
  background: #e5e7eb;
}

.task-item:hover .task-delete-btn {
  opacity: 1;
}

.task-item.active {
  background: #dbeafe;
}

.task-delete-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  border: none;
  border-radius: 4px;
  background: transparent;
  color: #9ca3af;
  cursor: pointer;
  opacity: 0;
  transition: all 0.15s;
  margin-left: auto;
}

.task-delete-btn:hover {
  background: #ef4444;
  color: #fff;
}

.task-file-icon {
  width: 16px;
  height: 16px;
  flex-shrink: 0;
  transition: width 0.2s ease, height 0.2s ease;
}

.task-file-icon.collapsed-icon {
  width: 20px;
  height: 20px;
}

.task-list-content.collapsed .task-item {
  justify-content: flex-start;
  gap: 6px;
  padding: 6px 8px;
  border-radius: 8px;
}

.task-list-content.collapsed .task-item.active {
  background: #dbeafe;
}

.task-list-content.collapsed .task-item:hover {
  background: #e5e7eb;
}

.task-item svg:first-child {
  color: #9ca3af;
  flex-shrink: 0;
}

.task-item.active svg:first-child {
  color: #0288d1;
}

.task-name {
  flex: 1;
  font-size: 13px;
  color: #374151;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.task-name-collapsed {
  font-size: 12px;
  color: #374151;
  line-height: 1;
  white-space: nowrap;
}

.task-item.active .task-name-collapsed {
  color: #0288d1;
}

.main-area {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.top-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 48px;
  padding: 0 20px;
  background: #fff;
  border-bottom: 1px solid #e8e8e8;
  flex-shrink: 0;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.page-title {
  font-size: 18px;
  font-weight: 600;
  color: #1a1a2e;
  margin: 0;
}

.page-subtitle-tag {
  font-size: 12px;
  color: #86909C;
  background: #f5f5f5;
  padding: 2px 8px;
  border-radius: 4px;
  margin-left: 8px;
  white-space: nowrap;
}

.mineru-tag {
  font-size: 12px;
  color: #666;
  margin-left: 8px;
  padding: 2px 8px;
  background: #f0f0f0;
  border-radius: 4px;
}

.header-right {
  display: flex;
  gap: 4px;
}

.ghost-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: #9ca3af;
  cursor: pointer;
  transition: all 0.2s;

  .star.filled {
    fill: #ffc107;
    color: #ffc107;
  }
}

.ghost-btn:hover {
  background: #f3f4f6;
  color: #374151;
}

.ghost-btn.active {
  color: #fa8c16;
}

.ghost-btn.active:hover {
  background: #fff7e6;
}

.back-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border: none;
  border-radius: 6px;
  background: #f5f5f5;
  color: #666;
  cursor: pointer;
  margin-right: 12px;
  transition: all 0.2s;
}

.back-btn:hover {
  background: #e8e8e8;
}

.parse-area {
  flex: 1;
  overflow-y: auto;
  padding: 24px 32px 32px;
  background: #fafbfc;
  background-image: radial-gradient(circle, #e0e0e0 1px, transparent 1px);
  background-size: 24px 24px;
}

.upload-dropzone {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 320px;
  padding: 48px 32px;
  background: #fff;
  border: 1px dashed #d9d9d9;
  border-radius: 16px;
  text-align: center;
  transition: border-color 0.2s ease, background-color 0.2s ease, box-shadow 0.2s ease;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
}

.upload-dropzone.drag-over {
  border-color: #1890ff;
  background-color: #f0f7ff;
  box-shadow: 0 0 0 3px rgba(24, 144, 255, 0.12);
}

@keyframes breathe {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.08); }
}

@keyframes breathe-fast {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.12); }
}

@keyframes swing-left {
  0%, 100% { transform: rotate(-3deg); }
  50% { transform: rotate(3deg); }
}

@keyframes swing-right {
  0%, 100% { transform: rotate(3deg); }
  50% { transform: rotate(-3deg); }
}

@keyframes swing-left-fast {
  0%, 100% { transform: rotate(-5deg); }
  50% { transform: rotate(5deg); }
}

@keyframes swing-right-fast {
  0%, 100% { transform: rotate(5deg); }
  50% { transform: rotate(-5deg); }
}

@keyframes success-bounce {
  0% { transform: scale(1); }
  30% { transform: scale(0.9); }
  60% { transform: scale(1.05); }
  100% { transform: scale(1); }
}

.upload-cloud-icon {
  margin-bottom: 24px;
  transition: transform 0.3s ease;
}

.upload-cloud-icon g {
  transition: opacity 0.5s ease, filter 0.5s ease;
}

.upload-cloud-icon .inactive {
  opacity: 0.3;
  animation: none !important;
  filter: grayscale(50%);
}

.upload-cloud-icon .active {
  opacity: 1;
}



.upload-cloud-icon .main-icon {
  animation: breathe 2s ease-in-out infinite;
  transform-origin: center center;
}

.upload-cloud-icon .side-icon-left {
  animation: swing-left 3s ease-in-out infinite;
  transform-origin: bottom right;
}

.upload-cloud-icon .side-icon-right {
  animation: swing-right 3s ease-in-out infinite;
  transform-origin: bottom left;
}

.upload-cloud-icon .active.side-icon-left {
  animation: swing-left 3s ease-in-out infinite;
}

.upload-cloud-icon .active.side-icon-right {
  animation: swing-right 3s ease-in-out infinite;
}

.upload-cloud-icon .active.main-icon {
  animation: breathe 2s ease-in-out infinite;
}

.upload-dropzone.drag-over .main-icon {
  animation: breathe-fast 1s ease-in-out infinite;
  opacity: 1;
  filter: none;
}

.upload-dropzone.drag-over .side-icon-left {
  animation: swing-left-fast 1s ease-in-out infinite;
  opacity: 1;
  filter: none;
}

.upload-dropzone.drag-over .side-icon-right {
  animation: swing-right-fast 1s ease-in-out infinite;
  opacity: 1;
  filter: none;
}

.upload-dropzone.drag-over .upload-cloud-icon {
  transform: translateY(-4px);
}

.upload-cloud-icon.uploaded .main-icon.active {
  animation: success-bounce 0.6s ease forwards;
}

.upload-cloud-icon.uploaded .main-icon.active path[fill="#FE5A4E"] {
  fill: #4CAF50;
  transition: fill 0.6s ease;
}

@media (prefers-reduced-motion: reduce) {
  .upload-cloud-icon .main-icon,
  .upload-cloud-icon .side-icon-left,
  .upload-cloud-icon .side-icon-right,
  .upload-cloud-icon .active.main-icon,
  .upload-cloud-icon .active.side-icon-left,
  .upload-cloud-icon .active.side-icon-right {
    animation: none;
  }
}

.upload-file-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 28px;
  border: none;
  border-radius: 8px;
  background: linear-gradient(135deg, #4fc3f7 0%, #0288d1 100%);
  color: #fff;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 2px 6px rgba(2, 136, 209, 0.3);
}

.upload-file-btn:hover {
  box-shadow: 0 4px 12px rgba(2, 136, 209, 0.4);
  transform: translateY(-1px);
}

.upload-dropzone.drag-over .upload-file-btn {
  box-shadow: 0 4px 12px rgba(2, 136, 209, 0.4);
}

.hidden-input {
  display: none;
}

.selected-files {
  margin-bottom: 24px;
}

.selected-file {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 16px;
  background: #f5f5f5;
  border-radius: 8px;
  margin-bottom: 8px;
}

.selected-file svg:first-child {
  color: #4fc3f7;
}

.selected-file span {
  flex: 1;
  font-size: 13px;
  color: #333;
}

.remove-file {
  padding: 4px;
  border: none;
  border-radius: 4px;
  background: transparent;
  color: #999;
  cursor: pointer;
  transition: all 0.2s;
}

.remove-file:hover {
  background: #e8e8e8;
  color: #666;
}

.uploading-status {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  color: #1890ff;
  font-size: 14px;
}

.loading-icon {
  animation: spin 1s linear infinite;
}

.config-section {
  max-width: none;
  margin: 24px 0 32px;
  padding: 24px;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
}

.config-header {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  font-weight: 600;
  color: #333;
  margin-bottom: 20px;
}

.config-options {
  display: flex;
  gap: 16px;
  margin-bottom: 24px;
}

.config-item {
  flex: 1;
}

.config-item label {
  display: block;
  font-size: 13px;
  color: #666;
  margin-bottom: 8px;
}

.switch-group {
  display: flex;
  align-items: center;
}

.parse-btn {
  width: 100%;
  padding: 12px;
  background: linear-gradient(135deg, #4fc3f7 0%, #0288d1 100%);
  color: #fff;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.parse-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(79, 195, 247, 0.4);
}

.parse-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.spin {
  animation: spin 1s linear infinite;
}

.compare-container {
  flex: 1;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0;
  overflow: hidden;
}

.left-panel,
.right-panel {
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.left-panel {
  background: #f0f0f0;
  border-right: 1px solid #d0d0d0;
}

.right-panel {
  background: #fff;
}

.panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  height: 48px;
  background: #fff;
  border-bottom: 1px solid #e8e8e8;
  flex-shrink: 0;
}

.panel-header-right {
  display: flex;
  align-items: center;
  gap: 12px;
}

.mindmap-actions-header {
  display: flex;
  align-items: center;
  gap: 12px;
}

.node-count {
  padding: 6px 14px;
  font-size: 12px;
  color: #6B7280;
  background: transparent;
  border-radius: 6px;
  cursor: default;
}

.header-actions {
  display: flex;
  gap: 4px;
}

.header-action-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: #9ca3af;
  cursor: pointer;
  transition: all 0.2s ease;
}

.header-action-btn:hover {
  background: #f3f4f6;
  color: #374151;
}

.mode-switch {
  display: flex;
  background: #f3f4f6;
  padding: 2px;
  border-radius: 6px;
}

.mode-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 28px;
  border: none;
  border-radius: 4px;
  background: transparent;
  color: #6b7280;
  cursor: pointer;
  transition: all 0.2s;
}

.mode-btn:hover:not(.active) {
  color: #374151;
}

.mode-btn.active {
  background: #fff;
  color: #111827;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}

.left-panel .panel-header {
  background: #f5f5f5;
}

.panel-title {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  font-weight: 600;
  color: #333;
}

.panel-controls {
  display: flex;
  align-items: center;
  gap: 12px;
}

.control-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border: 1px solid #d9d9d9;
  border-radius: 6px;
  background: #fff;
  color: #666;
  cursor: pointer;
  transition: all 0.2s;
}

.control-btn:hover:not(:disabled) {
  background: #f5f5f5;
}

.control-btn:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}

.zoom-controls {
  display: flex;
  align-items: center;
  gap: 8px;
  background: #fff;
  padding: 2px;
  border-radius: 6px;
  border: 1px solid #d9d9d9;
}

.zoom-value {
  font-size: 12px;
  color: #666;
  min-width: 45px;
  text-align: center;
}

.tab-container {
  display: flex;
  background: #f3f4f6;
  padding: 3px;
  border-radius: 8px;
  position: relative;
}

.tab-item {
  padding: 5px 14px;
  border: none;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  background: transparent;
  color: #6b7280;
  position: relative;
  z-index: 1;
}

.tab-item:hover:not(.active) {
  color: #374151;
}

.tab-item.active {
  background: #fff;
  color: #111827;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
}

.panel-content {
  flex: 1;
  overflow: hidden;
  padding: 0;
  display: flex;
  flex-direction: column;
  min-height: 0;
}

.panel-content.preview-area {
  overflow-y: auto;
  overflow-x: hidden;
}

.panel-content.result-content {
  position: relative !important;
  background: #fff;
  padding: 0 !important;
  overflow: hidden !important;
  flex: 1;
  display: flex;
  flex-direction: column;
  min-height: 0;
  height: 100%;
  margin: 0 !important;
}

.panel-content.result-content > .tab-content-wrapper {
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  bottom: 0 !important;
  display: flex !important;
  flex-direction: column;
  overflow: hidden !important;
  margin: 0 !important;
  padding: 0 !important;
}

.panel-content.result-content > .tab-content-wrapper > .fade-enter-active,
.panel-content.result-content > .tab-content-wrapper > .fade-leave-active {
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  bottom: 0 !important;
  display: flex !important;
  flex-direction: column;
}

.panel-content.result-content > .tab-content-wrapper > .fade-enter-active > .markdown-wrapper,
.panel-content.result-content > .tab-content-wrapper > .fade-leave-active > .markdown-wrapper,
.panel-content.result-content > .tab-content-wrapper > .markdown-wrapper {
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  bottom: 0 !important;
}

.panel-content.result-content > .tab-content-wrapper > .fade-enter-active > .mindmap-view,
.panel-content.result-content > .tab-content-wrapper > .fade-leave-active > .mindmap-view,
.panel-content.result-content > .tab-content-wrapper > .mindmap-view {
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  bottom: 0 !important;
}

.panel-content.result-content > .tab-content-wrapper > .fade-enter-active > .json-view,
.panel-content.result-content > .tab-content-wrapper > .fade-leave-active > .json-view,
.panel-content.result-content > .tab-content-wrapper > .json-view {
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  bottom: 0 !important;
  margin: 0 !important;
  padding: 0 !important;
  border: none !important;
}

.result-content {
  background: #fff;
  overflow: hidden;
  flex: 1;
  min-height: 0;
  padding: 0;
  margin: 0;
}

.result-content > div > p:first-child,
.result-content > div > h1:first-child,
.result-content > div > h2:first-child {
  margin-top: 0;
}

.pdf-pages-wrapper {
  width: 100%;
  min-height: 100%;
  padding: 10px;
  background: #fff;
  overflow-y: auto;
}

.pdf-page-container {
  margin-bottom: 10px;
  text-align: center;
}

.pdf-canvas {
  display: block;
  margin: 0 auto;
  max-width: 100%;
}

.pdf-fallback-image {
  display: block;
  margin: 0 auto;
  max-width: 100%;
  height: auto;
}

.image-preview-wrapper {
  background: #fff;
  min-height: 100%;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding: 20px 0;
}

.preview-image {
  max-width: 100%;
  object-fit: contain;
  border-radius: 4px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.office-preview-wrapper {
  width: 100%;
  height: 100%;
  min-height: 100%;
  background: #fff;
  border-radius: 4px;
  box-shadow: none;
  overflow: hidden;
}

.office-component {
  width: 100%;
  height: 100%;
  min-height: 100%;
}

.office-component :deep(.vue-office-pptx),
.office-component :deep(.vue-office-docx),
.office-component :deep(.vue-office-excel) {
  width: 100%;
  height: 100%;
}

.office-component :deep(.slide-container) {
  width: 100% !important;
  height: 100% !important;
}

.office-component :deep(.slide-item) {
  width: 100% !important;
  height: 100% !important;
}

.office-component :deep(.docx-container),
.office-component :deep(.excel-container) {
  width: 100%;
  height: 100%;
  overflow: auto;
}

.office-component :deep(.docx-container) *,
.office-component :deep(.excel-container) * {
  max-width: 100% !important;
}

.office-component :deep(.sheet-container),
.office-component :deep(.table-container) {
  width: 100% !important;
}

.office-component :deep(.slide-content),
.office-component :deep(.slide-inner) {
  width: 100% !important;
  height: 100% !important;
}

.pptx-tiled-wrapper {
  width: 100%;
  height: 100%;
  min-height: 600px;
  background: #fff;
  border-radius: 0;
  overflow: auto;
  padding: 16px;
  margin: 0;
}

.pptx-tiled-component {
  width: 100%;
  height: auto;
  min-height: 560px;
}

.pptx-tiled-component :deep(.vue-office-pptx) {
  width: 100%;
  height: auto;
  min-height: 560px;
  background: #fff;
  display: block;
}

.pptx-tiled-component :deep(.pptx-preview-wrapper) {
  background: #fff !important;
  width: 100% !important;
  height: auto !important;
  min-height: 500px !important;
  overflow: auto !important;
  display: block;
}

.pptx-tiled-component :deep(.pptx-preview-slide-wrapper) {
  width: 100% !important;
  max-width: none !important;
  margin: 0 0 16px 0 !important;
  padding: 0 !important;
  background: #fff !important;
  border-radius: 4px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
  overflow: hidden;
  display: block;
  position: relative;
  aspect-ratio: 4 / 3;
}

.pptx-tiled-component :deep(.pptx-preview-slide-wrapper) svg {
  width: 100% !important;
  height: 100% !important;
  object-fit: contain;
}

.pptx-tiled-component :deep(.pptx-preview-slide-wrapper) canvas {
  width: 100% !important;
  height: 100% !important;
  object-fit: contain;
}

.pptx-tiled-component :deep(.slide-content),
.pptx-tiled-component :deep(.slide-inner),
.pptx-tiled-component :deep(.slide-container) {
  width: 100% !important;
  height: 100% !important;
  max-width: none !important;
  max-height: none !important;
  min-height: 450px !important;
}

.pptx-tiled-component :deep(.slide-content) svg,
.pptx-tiled-component :deep(.slide-inner) svg,
.pptx-tiled-component :deep(.slide-container) svg {
  width: 100% !important;
  height: 100% !important;
  max-width: 100% !important;
  max-height: 100% !important;
}

.pptx-tiled-component :deep(.slide-content) canvas,
.pptx-tiled-component :deep(.slide-inner) canvas,
.pptx-tiled-component :deep(.slide-container) canvas {
  width: 100% !important;
  height: 100% !important;
  max-width: 100% !important;
  max-height: 100% !important;
}

.preview-loading-overlay,
.preview-error-overlay {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 16px;
  padding: 80px 0;
  color: #999;
}

.preview-loading-overlay .loading-icon {
  color: #1890ff;
}

.preview-error-overlay .error-icon {
  color: #ef5350;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
  flex: 1;
  display: flex;
  flex-direction: column;
  min-height: 0;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.result-content > div:last-child .markdown-wrapper,
.result-content > div:last-child .mindmap-view,
.result-content > div:last-child .json-view {
  flex: 1;
  min-height: 0;
}

.markdown-wrapper {
  flex: 1;
  width: 100%;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  min-height: 0;
  height: 100%;
}

.markdown-wrapper > textarea:first-child,
.markdown-editor {
  flex: 1;
  width: 100%;
  height: 100%;
  padding: 20px;
  border: none;
  outline: none;
  resize: none;
  font-family: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
  font-size: 14px;
  line-height: 1.6;
  background: #1e1e1e;
  color: #d4d4d4;
  box-sizing: border-box;
  display: block;
  overflow-y: auto;
}

.markdown-editor::placeholder {
  color: #6b7280;
}

.markdown-wrapper > div:first-child {
  flex: 1;
  width: 100%;
  overflow-y: auto;
  overflow-x: hidden;
  padding: 24px 32px;
  max-width: 100%;
  box-sizing: border-box;
  color: #4b5563;
  font-size: 15px;
  line-height: 1.8;
  word-wrap: break-word;
  overflow-wrap: break-word;
}

.markdown-wrapper > div:first-child > *:first-child {
  margin-top: 0 !important;
}

.markdown-wrapper > div:first-child > *:last-child {
  margin-bottom: 0 !important;
}

.markdown-wrapper > div:first-child h1 {
  font-size: 30px;
  font-weight: 700;
  color: #111827;
  margin-top: 32px;
  margin-bottom: 24px;
  padding-bottom: 12px;
  border-bottom: 1px solid #e5e7eb;
  line-height: 1.3;
}

.markdown-wrapper > div:first-child h2 {
  font-size: 23px;
  font-weight: 600;
  color: #1f2937;
  margin-top: 24px;
  margin-bottom: 16px;
  padding-bottom: 8px;
  border-bottom: 1px solid #f3f4f6;
  line-height: 1.35;
}

.markdown-wrapper > div:first-child h3 {
  font-size: 19px;
  font-weight: 600;
  color: #1f2937;
  margin-top: 20px;
  margin-bottom: 12px;
  line-height: 1.4;
}

.markdown-wrapper > div:first-child h4,
.markdown-wrapper > div:first-child h5,
.markdown-wrapper > div:first-child h6 {
  font-weight: 600;
  color: #374151;
  margin-top: 16px;
  margin-bottom: 10px;
  line-height: 1.4;
}

.markdown-wrapper > div:first-child h4 { font-size: 17px; }
.markdown-wrapper > div:first-child h5 { font-size: 15px; }
.markdown-wrapper > div:first-child h6 { font-size: 14px; color: #6b7280; }

.markdown-wrapper > div:first-child p {
  margin-top: 0;
  margin-bottom: 16px;
  line-height: 1.8;
}

.markdown-wrapper > div:first-child ul,
.markdown-wrapper > div:first-child ol {
  margin-top: 8px;
  margin-bottom: 16px;
  padding-left: 24px;
}

.markdown-wrapper > div:first-child li {
  margin-bottom: 6px;
  line-height: 1.7;
}

.markdown-wrapper > div:first-child li > ul,
.markdown-wrapper > div:first-child li > ol {
  margin-top: 4px;
  margin-bottom: 4px;
}

.markdown-wrapper > div:first-child blockquote {
  margin: 16px 0;
  padding: 12px 20px;
  border-left: 4px solid #d1d5db;
  background: #f9fafb;
  color: #4b5563;
  border-radius: 0 6px 6px 0;
}

.markdown-wrapper > div:first-child blockquote p {
  margin-bottom: 8px;
}

.markdown-wrapper > div:first-child blockquote p:last-child {
  margin-bottom: 0;
}

.markdown-wrapper > div:first-child table {
  width: 100%;
  border-collapse: collapse;
  margin: 16px 0;
  font-size: 14px;
  overflow: hidden;
  border-radius: 6px;
  border: 1px solid #e5e7eb;
}

.markdown-wrapper > div:first-child thead {
  background: #f3f4f6;
}

.markdown-wrapper > div:first-child th {
  padding: 10px 14px;
  text-align: left;
  font-weight: 600;
  color: #374151;
  border-bottom: 2px solid #e5e7eb;
}

.markdown-wrapper > div:first-child td {
  padding: 10px 14px;
  border-bottom: 1px solid #f3f4f6;
  color: #4b5563;
}

.markdown-wrapper > div:first-child tbody tr:last-child td {
  border-bottom: none;
}

.markdown-wrapper > div:first-child tbody tr:hover {
  background: #f9fafb;
}

.markdown-wrapper > div:first-child pre {
  margin: 16px 0;
  padding: 16px 20px;
  background: #1e1e1e;
  color: #d4d4d4;
  border-radius: 8px;
  overflow-x: auto;
  font-family: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
  font-size: 13px;
  line-height: 1.6;
}

.markdown-wrapper > div:first-child pre code {
  background: none;
  padding: 0;
  border-radius: 0;
  font-size: inherit;
  color: inherit;
}

.markdown-wrapper > div:first-child code {
  background: #f3f4f6;
  color: #e11d48;
  padding: 2px 6px;
  border-radius: 4px;
  font-family: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
  font-size: 0.9em;
}

.markdown-wrapper > div:first-child hr {
  border: none;
  height: 1px;
  background: #e5e7eb;
  margin: 24px 0;
}

.markdown-wrapper > div:first-child img {
  max-width: 100%;
  height: auto;
  border-radius: 6px;
  margin: 12px 0;
}

.markdown-wrapper > div:first-child a {
  color: #0288d1;
  text-decoration: none;
}

.markdown-wrapper > div:first-child a:hover {
  text-decoration: underline;
  color: #026aa7;
}

.markdown-wrapper > div:first-child strong {
  font-weight: 600;
  color: #1f2937;
}

.markdown-wrapper > div:first-child em {
  font-style: italic;
}

.result-content {
  background: #fff;
  overflow: hidden;
  flex: 1;
  min-height: 0;
  padding: 0;
  margin: 0;
}

.tab-content-wrapper {
  flex: 1;
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: column;
  min-height: 0;
  overflow: hidden;
}

/* 确保 Transition 动画容器也继承高度 */
.tab-content-wrapper > .fade-enter-active,
.tab-content-wrapper > .fade-leave-active,
.tab-content-wrapper .json-view,
.tab-content-wrapper .markdown-wrapper,
.tab-content-wrapper .mindmap-view {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-height: 0;
  width: 100%;
  height: 100%;
}

.result-content {
  background: #fff;
  overflow: hidden;
  flex: 1;
  min-height: 0;
  padding: 0;
  margin: 0;
}

.result-content .tab-content-wrapper {
  height: 100%;
  display: flex;
  flex-direction: column;
}

/* 当在标签页模式下，去掉padding让内容填满 */
.result-content:has(.tab-content-wrapper) {
  padding: 0;
  overflow: hidden;
}

.result-content > div > p:first-child,
.result-content > div > h1:first-child,
.result-content > div > h2:first-child {
  margin-top: 0;
}

.result-content p,
.result-content h1,
.result-content h2,
.result-content h3,
.result-content h4,
.result-content h5,
.result-content h6,
.result-content table {
  margin: 0;
}

.result-content h1 {
  font-size: 30px;
  font-weight: 700;
  margin: 56px 0 28px;
  padding-bottom: 16px;
  border-bottom: 2px solid #e5e7eb;
  color: #111827;
  letter-spacing: -0.02em;
  line-height: 1.3;
}

.result-content h1:first-child {
  margin-top: 0;
}

.result-content h2 {
  font-size: 24px;
  font-weight: 600;
  margin: 48px 0 24px;
  color: #1f2937;
  letter-spacing: -0.01em;
  line-height: 1.4;
}

.result-content h3 {
  font-size: 20px;
  font-weight: 600;
  margin: 36px 0 18px;
  color: #374151;
  line-height: 1.5;
}

.result-content h4 {
  font-size: 17px;
  font-weight: 600;
  margin: 28px 0 14px;
  color: #4b5563;
  line-height: 1.5;
}

.result-content h5 {
  font-size: 15px;
  font-weight: 600;
  margin: 24px 0 12px;
  color: #6b7280;
  line-height: 1.5;
}

.result-content h6 {
  font-size: 14px;
  font-weight: 600;
  margin: 20px 0 10px;
  color: #9ca3af;
  line-height: 1.5;
}

.result-content p {
  margin-bottom: 28px;
  line-height: 2;
  color: #4b5563;
  font-size: 16px;
}

.result-content ul,
.result-content ol {
  padding-left: 32px;
  margin-bottom: 28px;
}

.result-content li {
  margin-bottom: 14px;
  line-height: 2;
  color: #4b5563;
  font-size: 16px;
}

.result-content code {
  background: #f6ffed;
  color: #52c41a;
  padding: 4px 10px;
  border-radius: 5px;
  font-size: 13px;
  font-family: 'Fira Code', monospace;
}

.result-content pre {
  background: #2d2d2d;
  padding: 28px;
  border-radius: 12px;
  overflow-x: auto;
  margin: 32px 0;
}

.result-content pre code {
  background: none;
  color: #ccc;
  padding: 0;
  font-size: 14px;
  line-height: 1.7;
}

.result-content table {
  width: 100%;
  border-collapse: collapse;
  margin: 36px 0;
  border-radius: 8px;
  overflow: hidden;
}

.result-content th,
.result-content td {
  border: 1px solid #e8e8e8;
  padding: 16px 18px;
  text-align: left;
  line-height: 1.8;
}

.result-content th {
  background: #fafafa;
  font-weight: 600;
  color: #333;
}

.result-content a {
  color: #0288d1;
  text-decoration: none;
  border-bottom: 1px solid transparent;
  transition: all 0.2s;
}

.result-content a:hover {
  color: #01579b;
  border-bottom-color: #01579b;
}

.result-content img {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  margin: 28px 0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.result-content strong {
  font-weight: 700;
  color: #1f2937;
}

.result-content em {
  font-style: italic;
  color: #374151;
}

.result-content blockquote {
  border-left: 6px solid #4fc3f7;
  padding: 20px 24px;
  margin: 28px 0;
  background: #f0f9ff;
  border-radius: 0 12px 12px 0;
  color: #555;
  line-height: 1.8;
}

.result-content hr {
  border: none;
  height: 2px;
  background: #e8e8e8;
  margin: 32px 0;
}

.loading-state,
.error-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 80px 0;
}

.error-state p {
  color: #f5222d;
  font-size: 16px;
  margin-bottom: 20px;
}

.error-action {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 24px;
  background: linear-gradient(135deg, #4fc3f7 0%, #0288d1 100%);
  color: #fff;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s;
}

.error-action:hover {
  background: #40a9ff;
}

.mindmap-view {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  min-height: 0;
}

.mindmap-container {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  background-color: #F9FAFC;
  overflow: hidden;
  min-height: 0;
}

.mindmap-content {
  flex: 1;
  width: 100%;
  height: 100%;
  overflow: hidden;
  position: relative;
  background-color: #F9FAFC;
  cursor: grab;
  min-height: 0;
  display: flex;
  align-items: stretch;
  justify-content: stretch;
}

.mindmap-content:active {
  cursor: grabbing;
}

.markmap-svg {
  width: 100%;
  height: 100%;
  display: block;
  background-color: #fff;
  min-height: 0;
}

.json-view {
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  bottom: 0 !important;
  width: 100% !important;
  height: 100% !important;
  display: flex !important;
  flex-direction: column;
  overflow: hidden !important;
  padding: 0 !important;
  margin: 0 !important;
  box-sizing: border-box;
}

.json-code {
  background: #2d2d2d;
  color: #ccc;
  padding: 0 !important;
  border-radius: 0 !important;
  overflow: auto;
  font-size: 13px;
  font-family: 'Fira Code', monospace;
  white-space: pre-wrap;
  word-break: break-all;
  flex: 1 !important;
  width: 100% !important;
  min-height: 0 !important;
  height: 100% !important;
  margin: 0 !important;
  box-sizing: border-box;
}

@media (max-width: 1024px) {
  .compare-container {
    grid-template-columns: 1fr;
  }

  .left-panel {
    border-right: none;
    border-bottom: 1px solid #d0d0d0;
  }

  .panel-header {
    padding: 10px 16px;
  }

  .panel-content:not(.result-content) {
    padding: 16px;
  }
}

@media (max-width: 768px) {
  .sidebar {
    width: 60px;
  }

  .nav-item span,
  .logo span,
  .task-list-header span,
  .task-name {
    display: none;
  }

  .top-header {
    padding: 12px 16px;
  }

  .page-title {
    font-size: 16px;
  }

  .header-btn span {
    display: none;
  }

  .parse-area {
    padding: 16px;
  }

  .upload-dropzone {
    min-height: 280px;
    padding: 32px 16px;
  }

  .config-options {
    flex-direction: column;
  }
}

.ai-summary-toggle {
  display: flex;
  align-items: center;
  gap: 8px;
}

.ai-summary-label {
  font-size: 12px;
  color: #6b7280;
  font-weight: 500;
  white-space: nowrap;
}

.ai-refresh-btn {
  width: 28px !important;
  height: 28px !important;
}

.ai-refresh-btn svg {
  animation: none;
}

.ai-loading-state,
.ai-error-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  width: 100%;
  height: 100%;
  background: #F9FAFC;
}

.ai-loading-state .loading-icon {
  color: #0288d1;
}

.ai-loading-text {
  font-size: 14px;
  color: #6b7280;
  margin: 0;
}

.ai-error-state .error-icon {
  color: #ef5350;
}

.ai-error-text {
  font-size: 13px;
  color: #ef5350;
  margin: 0;
  max-width: 280px;
  text-align: center;
}

</style>
