<template>
  <div class="Guide">
    <page-header class="mb-3">
      {{ $t('感染症対策について') }}
    </page-header>
    <StaticCard>
      <i18n
        path="このページの内容は、神戸市公式ホームページの {link} に移動しました。"
        tag="p"
      >
        <template v-slot:link>
          <a
            href="https://www.city.kobe.lg.jp/a73576/kenko/health/infection/protection/coronavirus_houshin_taisaku.html"
            target="_blank"
            rel="noopener noreferrer"
          >
            {{ $t('対応方針・対策本部員会議資料') }}
          </a>
        </template>
      </i18n>
    </StaticCard>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { MetaInfo } from 'vue-meta'
import StaticCard from '@/components/StaticCard.vue'
import PageHeader from '@/components/PageHeader.vue'

export default Vue.extend({
  components: {
    PageHeader,
    StaticCard
  },
  head(): MetaInfo {
    return {
      title: this.$t('感染症対策について') as string
    }
  }
})
</script>
