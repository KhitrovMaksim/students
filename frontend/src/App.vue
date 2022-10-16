<template>
  <div>
    <the-header></the-header>
    <router-view></router-view>
  </div>
</template>

<script>
import TheHeader from "@/components/layout/TheHeader";

export default {
  name: "App.vue",
  components: {
    TheHeader
  }

}
</script>

<style scoped>

</style>