<template>
  <div class="Guide">
    <page-header class="mb-3">
      {{ $t('感染症対策について') }}
    </page-header>
    <StaticCard>
      <h3>{{ $t('緊急事態宣言が発令されました。') }}</h3>
      <p>
        {{
          $t(
            '感染拡大防止のためには、人と人との接触をできる限り減らすことが重要であり、8割程度の接触機会の低減を目指す必要があります。市民のお一人おひとりが自ら感染者にならないこと、他人を感染させないため、徹底した行動変容にご協力いただくことが不可欠です。以下の事項を守っていただくよう、市長として市民の皆さまに要請します。'
          )
        }}
      </p>
      <ol>
        <li>
          {{ $t('生活の維持に必要な場合を除き、みだりに家から外出しないこと') }}
        </li>
        <li>
          {{ $t('東京、大阪などの人口密集地との不要不急の往来を行わないこと') }}
        </li>
        <li>
          {{
            $t(
              '通勤などにより 2. のエリアとやむを得ず往来する場合も、人混みには立ち寄らないなど感染防止のための行動をとること'
            )
          }}
        </li>
        <li>
          {{
            $t(
              '夜間から早朝にかけて営業し接客を伴う飲食店、カラオケなどの利用をしないこと'
            )
          }}
        </li>
        <li>
          {{ $t('不要不急の帰省や旅行など都道府県をまたいだ移動をしないこと') }}
        </li>
        <li>
          {{ $t('不要不急の会合や家族以外の大人数での会食などを行わないこと') }}
        </li>
        <li>
          {{
            $t(
              '「三つの密」（密閉・密集・密接）が重なる懸念のある集会・イベントに参加しないこと'
            )
          }}
        </li>
        <li>
          {{
            $t(
              '食料、医薬品、生活必需品について、無用な買いだめ、買い占めを行わず、冷静な行動をとること'
            )
          }}
        </li>
      </ol>
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
