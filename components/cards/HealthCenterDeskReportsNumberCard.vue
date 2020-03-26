<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-stacked-bar-chart
      :title="$t('保健所・保健センターでの一般相談件数')"
      :title-id="'number-of-reports-to-health-center-desk'"
      :chart-id="'time-stacked-bar-chart-center-contacts'"
      :chart-data="healthCenterGraph"
      :date="Data.health_center_summary.date"
      :items="healthCenterItems"
      :labels="healthCenterLabels"
      :unit="$t('件.reports')"
      :data-labels="healthCenterDataLabels"
    />
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
    // 保健所・保健センターの日別相談件数
    const healthCenterGraph = [
      Data.health_center_summary.data['保健センター'],
      Data.health_center_summary.data['予防衛生課']
    ]
    const healthCenterItems = [this.$t('保健センター'), this.$t('予防衛生課')]
    const healthCenterLabels = Data.health_center_summary.labels
    const healthCenterDataLabels = [
      this.$t('保健センター'),
      this.$t('予防衛生課')
    ]

    const data = {
      Data,
      healthCenterGraph,
      healthCenterItems,
      healthCenterLabels,
      healthCenterDataLabels
    }
    return data
  }
}
</script>
