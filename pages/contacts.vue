<template>
  <div class="Contacts">
    <page-header class="mb-3">
      {{ $t('神戸市電話相談窓口') }}
    </page-header>
    <StaticCard>
      <i18n
        path="このページの内容は、神戸市公式ホームページの {link} に移動しました。"
        tag="p"
      >
        <template v-slot:link>
          <a
            href="https://www.city.kobe.lg.jp/a73576/kenko/health/infection/protection/coronavirus.html#soudansaki"
            target="_blank"
            rel="noopener noreferrer"
          >
            {{ $t('新型コロナウイルスについて') }}
          </a>
        </template>
      </i18n>
    </StaticCard>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { MetaInfo } from 'vue-meta'
import PageHeader from '@/components/PageHeader.vue'
import StaticCard from '@/components/StaticCard.vue'

export default Vue.extend({
  components: {
    PageHeader,
    StaticCard
  },
  head(): MetaInfo {
    return {
      title: this.$t('神戸市電話相談窓口') as string
    }
  }
})
</script>
