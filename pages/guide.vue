<template>
  <div class="Guide">
    <page-header class="mb-3">
      {{ $t('感染症対策について') }}
    </page-header>
    <StaticCard>
      <!-- @todo hタグが存在しないのはHTML5として問題ないか-->
      <!-- <h3></h3> -->
      <ul>
        <li>
          <i18n
            path="{massInfection}を生み出さないようにすることが極めて重要です。"
          >
            <template v-slot:massInfection>
              <span>{{ $t('集団感染') }}</span>
            </template>
          </i18n>
        </li>
        <li>
          {{
            $t(
              '発熱、咳、だるさなど風邪の症状が出たら、仕事や学校を休み、くれぐれも人が集まる場所に外出しないでください。'
            )
          }}
        </li>
      </ul>
    </StaticCard>
    <StaticCard>
      <h3>{{ $t('集団感染を防ぐために') }}</h3>
      <ol>
        <li>
          {{ $t('換気の悪い「密閉」空間') }}
        </li>
        <li>
          {{ $t('多数が集まる「密集」場所') }}
        </li>
        <li>
          {{ $t('間近で会話や発生をする「密接」場面') }}
        </li>
      </ol>
      <p>{{ $t('という３つの「密」が同時に重なった場は避けましょう。') }}</p>
    </StaticCard>
    <StaticCard>
      <h3>{{ $t('感染症対策3つの基本') }}</h3>
      <ol>
        <li>
          {{ $t('こまめな手洗いをしよう') }}
        </li>
        <li>
          {{ $t('咳エチケットに努めよう') }}
        </li>
        <li>
          {{ $t('発熱等の風邪症状の時は外出を控えよう') }}
        </li>
      </ol>
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
