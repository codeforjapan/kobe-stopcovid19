<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-bar-chart
      :title="$t('健康相談窓口(帰国者・接触者相談センター) 相談件数')"
      :title-id="'number-of-reports-to-health-consultation-desk'"
      :chart-id="'time-bar-chart-window-contacts'"
      :chart-data="contactsGraph"
      :date="Data.contacts_summary.date"
      :unit="$t('件.reports')"
      :url="'https://data.city.kobe.lg.jp/data/dataset/32576-7-2-3-3'"
    />
    <!-- 件.reports = 窓口相談件数 -->
  </v-col>
</template>

<script>
import Data from '@/data/data.json'
import formatGraph from '@/utils/formatGraph'
import TimeBarChart from '@/components/TimeBarChart.vue'

export default {
  components: {
    TimeBarChart
  },
  data() {
    // 健康相談窓口(帰国者・接触者相談センター) 相談件数
    const contactsGraph = formatGraph(Data.contacts_summary.data)

    const data = {
      Data,
      contactsGraph
    }
    return data
  }
}
</script>
