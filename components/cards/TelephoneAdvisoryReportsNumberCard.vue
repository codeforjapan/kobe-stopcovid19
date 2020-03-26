<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-bar-chart
      :title="$t('新型コロナ健康相談窓口 相談件数')"
      :title-id="'number-of-reports-to-covid19-telephone-advisory-center'"
      :chart-id="'time-bar-chart-window-contacts'"
      :chart-data="windowContactsGraph"
      :date="Data.window_contacts.date"
      :unit="$t('件.reports')"
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
    // 新型コロナ健康相談窓口 相談件数
    const windowContactsGraph = formatGraph(Data.window_contacts.data)

    const data = {
      Data,
      windowContactsGraph
    }
    return data
  }
}
</script>
