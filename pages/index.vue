<template>
  <div class="MainPage">
    <div class="Header mb-3">
      <page-header :icon="headerItem.icon">
        {{ headerItem.title }}
      </page-header>
      <div class="UpdatedAt">
        <span>{{ $t('最終更新') }} </span>
        <time :datetime="updatedAt">{{ Data.lastUpdate }}</time>
      </div>
      <div
        v-show="!['ja', 'ja-basic'].includes($i18n.locale)"
        class="Annotation"
      >
        <span>{{ $t('注釈') }} </span>
      </div>
    </div>
    <whats-new class="mb-4" :items="newsItems" />
    <div class="mb-4" style="margin-top:50px">
      <p style="font-size:1.875rem;">
        「新型コロナウイルス感染症対策サイト」は2020年6月1日より神戸市公式ホームページに統合しました。<br />
      </p>
      <p>
        新URL：<a
          href="https://www.city.kobe.lg.jp/a73576/kenko/health/infection/protection/covid_19.html"
          >https://www.city.kobe.lg.jp/a73576/kenko/health/infection/protection/covid_19.html</a
        >
      </p>
    </div>
    <v-row class="DataBlock">
      <confirmed-cases-details-card />
      <!--<tested-cases-details-card />-->
      <confirmed-cases-attributes-card />
      <confirmed-cases-number-card />
      <!--<inspection-persons-number-card />-->
      <tested-number-card />
      <telephone-advisory-reports-number-card />
      <!--<consultation-desk-reports-number-card />
      <metro-card />
      <agency-card />-->
      <health-center-desk-reports-number-card />
    </v-row>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { MetaInfo } from 'vue-meta'
import PageHeader from '@/components/PageHeader.vue'
import Data from '@/data/data.json'
import News from '@/data/news.json'
// import TestedCasesDetailsCard from '@/components/cards/TestedCasesDetailsCard.vue'
// import InspectionPersonsNumberCard from '@/components/cards/InspectionPersonsNumberCard.vue'
/*
import ConsultationDeskReportsNumberCard from '@/components/cards/ConsultationDeskReportsNumberCard.vue'
import MetroCard from '@/components/cards/MetroCard.vue'
import AgencyCard from '@/components/cards/AgencyCard.vue'
 */
import { convertDatetimeToISO8601Format } from '@/utils/formatDate'

export default Vue.extend({
  components: {
    PageHeader
  },
  data() {
    const data = {
      Data,
      headerItem: {
        icon: 'mdi-chart-timeline-variant',
        title: this.$t('神戸市市内の最新感染動向')
      },
      newsItems: News.newsItems
    }
    return data
  },
  computed: {
    updatedAt() {
      return convertDatetimeToISO8601Format(this.$data.Data.lastUpdate)
    }
  },
  head(): MetaInfo {
    return {
      title: this.$t('神戸市市内の最新感染動向') as string
    }
  }
})
</script>

<style lang="scss" scoped>
.MainPage {
  .Header {
    display: flex;
    flex-wrap: wrap;
    align-items: flex-end;

    @include lessThan($small) {
      flex-direction: column;
      align-items: baseline;
    }
  }

  .UpdatedAt {
    @include font-size(14);

    color: $gray-3;
    margin-bottom: 0.2rem;
  }

  .Annotation {
    @include font-size(12);

    color: $gray-3;
    @include largerThan($small) {
      margin: 0 0 0 auto;
    }
  }
  .DataBlock {
    margin: 20px -8px;

    .DataCard {
      @include largerThan($medium) {
        padding: 10px;
      }

      @include lessThan($small) {
        padding: 4px 8px;
      }
    }
  }
}
</style>
