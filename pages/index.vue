<template>
  <div class="MainPage">
    <div class="Header mb-3">
      <page-header :icon="headerItem.icon">
        {{ headerItem.title }}
      </page-header>
    </div>
    <div class="mb-4" style="margin-top:50px">
      <p style="font-size:1.875rem;">
        「新型コロナウイルス感染症対策サイト」は2020年6月1日より神戸市公式ホームページに統合しました。<br />
      </p>
      <p>
        新URL：<a
          href="https://www.city.kobe.lg.jp/a73576/kenko/health/infection/protection/covid_19.html"
          >https://www.city.kobe.lg.jp/a73576/kenko/health/infection/protection/covid_19.html</a
        >
      </p>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { MetaInfo } from 'vue-meta'
import PageHeader from '@/components/PageHeader.vue'

export default Vue.extend({
  components: {
    PageHeader
  },
  data() {
    const data = {
      headerItem: {
        icon: 'mdi-chart-timeline-variant',
        title: this.$t('神戸市市内の最新感染動向')
      }
    }
    return data
  },
  head(): MetaInfo {
    return {
      title: this.$t('神戸市市内の最新感染動向') as string
    }
  }
})
</script>

<style lang="scss" scoped>
.MainPage {
  .Header {
    display: flex;
    flex-wrap: wrap;
    align-items: flex-end;

    @include lessThan($small) {
      flex-direction: column;
      align-items: baseline;
    }
  }
}
</style>
