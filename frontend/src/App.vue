<template>
  <div class="content">
    <the-header></the-header>
    <router-view></router-view>
    <the-footer></the-footer>
  </div>
</template>

<script>
import TheHeader from "@/components/layout/TheHeader";
import TheFooter from "@/components/layout/TheFooter";

export default {
  name: "App.vue",
  components: {
    TheFooter,
    TheHeader
  }

}
</script>

<style scoped>

</style>