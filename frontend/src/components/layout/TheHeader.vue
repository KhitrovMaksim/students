<template>
  <div class="p-3 text-bg-dark">
    <header class="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-3 mb-4 border-bottom">
      <router-link to="/students" class="d-flex align-items-center mb-2 mb-lg-0 text-white text-decoration-none">
        <font-awesome-icon icon="fa-solid fa-graduation-cap" size="2xl"/>
      </router-link>
      <ul class="nav col-12 col-lg-auto mb-2 justify-content-center mb-md-0">
        <li><router-link to="/students" class="nav-link px-2 link-secondary">List of students</router-link></li>
        <li><router-link to="#" class="nav-link px-2 text-white">About</router-link></li>
        <li><router-link to="#" class="nav-link px-2 text-white">Statistics</router-link></li>
      </ul>

      <div class="col-md-3 text-end">
        <button type="button" class="btn btn-outline-light me-2">Add 20 Students</button>
        <button type="button" class="btn btn-warning">Clear All</button>
      </div>
    </header>
  </div>
</template>

<script>
export default {
  name: "TheHeader"
}
</script>

<style scoped>

</style>