<template>
  <div>
		<Location v-for="(location, index) in locationData" :key="location.name" :data="location" :index="index" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Location from './Location.vue';

let locationData = ref([]);

onMounted(() => {
  fetch('https://pantherfi.wilsonbiggs.com/api')
    .then(response => {
      if (!response.ok) {
        console.error('Is remote down?');
      } else {
        return response.json();
      }
    }).then(json => {
      let locations = [];
      for (const json_loc of json) {
        const obs = {
          down: [],
          up: [],
          ping: []
        };
        for (const observation of json_loc.obs) {
          obs.down.push([observation.timestamp * 1000, observation.download]);
          obs.up.push([observation.timestamp * 1000, observation.upload]);
          obs.ping.push([observation.timestamp * 1000, observation.ping]);
        }
        locations.push({
          name: json_loc.name,
          obs,
          curr_status: json_loc.curr_status
        });
      }
      locationData.value = locations;
    })
    .catch(error => {
      console.error('There has been a problem with your fetch operation:', error);
    });
})
</script>

<style>

</style>