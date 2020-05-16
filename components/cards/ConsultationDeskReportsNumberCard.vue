<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-bar-chart
      :title="$t('帰国者・接触者相談センター 相談件数')"
      :title-id="'number-of-reports-to-returnee-contact-center'"
      :chart-id="'time-bar-chart-center-contacts'"
      :chart-data="centerContactsGraph"
      :date="Data.center_contacts.date"
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
    // 帰国者・接触者相談センター 相談件数
    const centerContactsGraph = formatGraph(Data.center_contacts.data)

    const data = {
      Data,
      centerContactsGraph
    }
    return data
  }
}
</script>
