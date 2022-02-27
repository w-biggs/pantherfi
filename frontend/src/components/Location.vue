<template>
  <div class="location" :expanded="expandState">
    <h2>{{ data.name }}</h2>
    <div class="status">
      <span class="location-info-type">Status:</span>
      <span class="status-value" :status="data.curr_status.status">{{ statusStrings[data.curr_status.status] }}</span>
    </div>
    <div class="speed">
      <span class="location-info-type">Speed:</span>
      <span>{{data.curr_status.status === 'up' ? `${Math.round(data.curr_status.down)}↓ ${Math.round(data.curr_status.up)}↑` : '--'}}</span>
    </div>
    <div class="ping">
      <span class="location-info-type">Ping:</span>
      <span>{{data.curr_status.status === 'up' ? `${Math.round(data.curr_status.ping)}ms` : '--'}}</span>
    </div>
    <div class="toggle">
      <button @click="expand()">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Pro 6.0.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M224 416c-8.188 0-16.38-3.125-22.62-9.375l-192-192c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0L224 338.8l169.4-169.4c12.5-12.5 32.75-12.5 45.25 0s12.5 32.75 0 45.25l-192 192C240.4 412.9 232.2 416 224 416z"/></svg>
      </button>
    </div>
    <div class="graphs">
      <div :id="`down-graph-${index}`"></div>
      <div :id="`up-graph-${index}`"></div>
      <div :id="`ping-graph-${index}`"></div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, toRaw } from 'vue';
import Highcharts from 'highcharts'; 
import BrokenAxis from 'highcharts/modules/broken-axis';

const props = defineProps({
  data: Object,
  index: Number
});

const buildChartOptions = function buildChartOptions(units, data) {
  return {
    title: undefined,
    legend: {
      enabled: false
    },
    plotOptions: {
      series: {
        gapUnit: 1000,
        gapSize: 5,
        enableMouseTracking: false,
        states: {
          hover: {
            enabled: false
          }
        }
      }
    },
    chart: {
      backgroundColor: 'transparent',
      height: '15%'
    },
    xAxis: {
      tickInterval: (10 * 60 * 1000),
      type: 'datetime',
      max: new Date().getTime(),
      min: new Date().getTime() - (2 * 60 * 60 * 1000),
    },
    yAxis: {
      title: {
        text: units
      }
    },
    series: [{
      data: toRaw(data),
      marker: {
        enabled: true,
        fillColor: 'rgba(255,255,255,0.25)',
        radius: 1
      }
    }]
  };
};

onMounted(() => {
  BrokenAxis(Highcharts);
  Highcharts.chart(`down-graph-${props.index}`, buildChartOptions('Download (mbps)', props.data.obs.down));
  Highcharts.chart(`up-graph-${props.index}`, buildChartOptions('Upload (mbps)', props.data.obs.up));
  Highcharts.chart(`ping-graph-${props.index}`, buildChartOptions('Ping (ms)', props.data.obs.ping));
});

const statusStrings = {
  up: 'Up',
  down: 'Down'
};

const expandState = ref(false);

const expand = function expand() {
  expandState.value = !expandState.value;
}
</script>

<style lang="scss">
  div.location {
    border-bottom: rgba(255,255,255,0.5) 1px solid;
    padding: 1rem 0.5rem;
    display: grid;
    grid-template-columns: 1fr repeat(4, auto);
    grid-template-areas:
      "name     status  speed   ping    toggle"
      "graphs   graphs  graphs  graphs  graphs";
    column-gap: 1rem;
    line-height: 1;

    &:first-of-type {
      border-top: rgba(255,255,255,0.5) 1px solid;
    }

    h2 {
      padding-right: .5em;
    }

    & > div {
      display: flex;
      align-items: center;
      justify-content: center;
    }
    
    .location-info-type {
      margin-right: .5em;
    }

    .status {
      grid-area: status;

      .status-value {
        display: inline-block;
        font-size: 0.8rem;
        padding: 0.2rem 0.3rem;
        border-radius: 0.2rem;
        //margin-bottom: -0.2rem;
        background: rgba(255,255,255,0.1);

        &[status=up] {
          background: #2fcc66;
          color: black;
        }

        &[status=down] {
          background: #e74c3c;
        }
      }
    }

    .speed {
      grid-area: speed;
    }

    .ping {
      grid-area: ping;
    }

    .toggle {
      grid-area: toggle;

      button {
        background: none;
        color: inherit;
        border: none;
        cursor: pointer;
        
        svg {
          fill: currentColor;
          height: 1rem;
        }
      }
    }

    .graphs {
      display: none;
      grid-area: graphs;
    }

    &[expanded=true] {
      row-gap: 1rem;

      .toggle button {
        transform: scaleY(-1);
      }

      .graphs {
        display: block;
      }
    }

    @media screen and (max-width: 800px) {
      grid-template-columns: repeat(4, auto);
      grid-template-areas:
        "name     name    name    toggle"
        "status   speed    ping   _"
        "graphs   graphs  graphs  graphs";
      row-gap: 1rem;

      h2 {
        grid-area: name;
      }
    }
  }
</style>