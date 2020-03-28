<template>
  <div class="Parent">
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
          {{ $t('換気が悪い、不特定多数の人が密集して過ごす空間は避けよう') }}
        </li>
        <li>
          {{ $t('風通しの良い空間づくりを心がけよう') }}
        </li>
      </ol>
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
