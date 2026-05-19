import { defineStore } from 'pinia';

export const useConfigStore = defineStore('config', {
  state: () => ({
    backend: 'hybrid-auto-engine',
    parseMethod: 'auto',
    lang: 'ch',
    startPage: 0,
    endPage: null,
    formulaEnable: true,
    tableEnable: true,
    imageAnalysis: true,
    asyncMode: false,
    returnMd: true,
    returnImages: false,
    responseFormatZip: false,
  }),

  getters: {
    requestOptions: (state) => ({
      backend: state.backend,
      parse_method: state.parseMethod,
      lang_list: [state.lang],
      start_page_id: state.startPage,
      end_page_id: state.endPage || '',
      formula_enable: state.formulaEnable,
      table_enable: state.tableEnable,
      image_analysis: state.imageAnalysis,
      return_md: state.returnMd,
      return_images: state.returnImages,
      response_format_zip: state.responseFormatZip,
    }),
  },

  actions: {
    updateConfig(config) {
      Object.assign(this, config);
    },

    resetConfig() {
      this.backend = 'hybrid-auto-engine';
      this.parseMethod = 'auto';
      this.lang = 'ch';
      this.startPage = 0;
      this.endPage = null;
      this.formulaEnable = true;
      this.tableEnable = true;
      this.imageAnalysis = true;
      this.asyncMode = false;
      this.returnMd = true;
      this.returnImages = false;
      this.responseFormatZip = false;
    },
  },
});
