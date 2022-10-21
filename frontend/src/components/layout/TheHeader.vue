<template>
  <header class="p-3 text-bg-dark">
    <div class="container">
      <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-between">

        <router-link to="/students" class="mb-2 text-white text-decoration-none">
          <font-awesome-icon icon="fa-solid fa-graduation-cap" size="2xl"/>
          <strong>&nbsp; Students</strong>
        </router-link>

        <ul class="nav col-12 col-lg-auto mb-2 justify-content-center mb-md-0">
          <li><router-link to="/students" :class="classForStudentsLink">List of students</router-link></li>
          <li><router-link to="/about" :class="classForAboutLink">About</router-link></li>
        </ul>

        <div class="text-end">
          <button type="button" class="btn btn-outline-light me-2" @click="addTwenty">Add 20 Students</button>
          <button type="button" class="btn btn-warning" @click="removeAll">Clear All</button>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: "TheHeader",
  computed: {
    classForStudentsLink() {
      if (this.$router.currentRoute.value.fullPath === '/students') {
        return 'nav-link px-2 link-secondary'
      } else {
        return 'nav-link px-2 text-white'
      }
    },
    classForAboutLink() {
      if (this.$router.currentRoute.value.fullPath === '/about') {
        return 'nav-link px-2 link-secondary'
      } else {
        return 'nav-link px-2 text-white'
      }
    }
  },
  methods: {
    removeAll() {
      this.$store.dispatch('students/removeAllStudents')
      this.$router.push('/students')
    },
    addTwenty() {
      this.$store.dispatch('students/addTwenty')
      this.$router.push('/students')
    }
  }
}
</script>

<style scoped>

</style>