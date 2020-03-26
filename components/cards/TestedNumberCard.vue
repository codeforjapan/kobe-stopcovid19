<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-stacked-bar-chart
      :title="$t('市内でのPCR検査件数及びその内訳')"
      :title-id="'number-of-tested'"
      :chart-id="'time-stacked-bar-chart-inspections'"
      :chart-data="inspectionsGraph"
      :date="Data.inspections_summary.date"
      :items="inspectionsItems"
      :labels="inspectionsLabels"
      :unit="$t('人')"
      :data-labels="inspectionsDataLabels"
      :url="
        'https://www.city.kobe.lg.jp/a73576/kenko/health/infection/protection/covid_19.html'
      "
    >
      <!-- 件.tested = 検査数 -->
      <!--<template v-if="$i18n.locale !== 'ja-basic'" v-slot:additionalNotes>
        {{ $t('※1: 疑い例・接触者調査') }}
        <br />
        {{ $t('※2: チャーター便・クルーズ船') }}
      </template>-->
    </time-stacked-bar-chart>
  </v-col>
</template>

<script>
import Data from '@/data/data.json'
import TimeStackedBarChart from '@/components/TimeStackedBarChart.vue'

export default {
  components: {
    TimeStackedBarChart
  },
  data() {
    // 検査実施日別状況
    const inspectionsGraph = [
      Data.inspections_summary.data['陽性確認者'],
      Data.inspections_summary.data['陰性確認者']
    ]
    const inspectionsItems = [this.$t('陽性確認者'), this.$t('陰性確認者')]
    const inspectionsLabels = Data.inspections_summary.labels
    const inspectionsDataLabels = [this.$t('陽性確認者'), this.$t('陰性確認者')]

    const data = {
      Data,
      inspectionsGraph,
      inspectionsItems,
      inspectionsLabels,
      inspectionsDataLabels
    }
    return data
  }
}
</script>
