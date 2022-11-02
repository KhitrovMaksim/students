<template>
  <main class="container mt-4">
    <div class="card">
      <div class="card-body text-center">
        <h1 class="card-title"><font-awesome-icon icon="fa-solid fa-user-tie" /></h1>
        <p class="card-text">The student with id: {{ this.$route.params.id }}</p>
      </div>
      <div class="card-body">
        <div class="row">
          <div class="col-sm-3">
            <h6 class="mb-0">First name:</h6>
          </div>
          <div class="col-sm-9 text-secondary"> {{ selectedStudent.first_name }}</div>
        </div>
        <hr>
        <div class="row">
          <div class="col-sm-3">
            <h6 class="mb-0">Last name:</h6>
          </div>
          <div class="col-sm-9 text-secondary"> {{ selectedStudent.last_name }}</div>
        </div>
        <hr>
        <div class="row">
          <div class="col-sm-3">
            <h6 class="mb-0">Date of birth:</h6>
          </div>
          <div class="col-sm-9 text-secondary"> {{ selectedStudent.date_of_birth}}</div>
        </div>
        <hr>
        <div class="row">
          <div class="col-sm-3">
            <h6 class="mb-0">Email address:</h6>
          </div>
          <div class="col-sm-9 text-secondary"> {{ selectedStudent.email }}</div>
        </div>
        <hr>
        <div class="row">
          <div class="col-sm-3">
            <h6 class="mb-0">Phone number: </h6>
          </div>
          <div class="col-sm-9 text-secondary"> {{ selectedStudent.phone }}</div>
        </div>
        <hr>
        <div class="row">
          <div class="col-sm-3">
            <h6 class="mb-0">Favorite sports: </h6>
          </div>
          <div class="col-sm-9 text-secondary">
              <span v-for="sport in selectedStudent.favorite_sports.split(', ')" :key="sport" >
                {{ sport }}<br>
              </span>
          </div>
        </div>
        <hr>
        <div class="card-body">
            <router-link to="/students" class="btn btn-outline-primary">Back to list</router-link>
            <router-link :to="`/students/${this.$route.params.id}/edit`" class="btn btn-outline-warning mx-2">Edit</router-link>
            <button class="btn btn-outline-danger" @click="remove(selectedStudent.id)">Delete</button>
        </div>
      </div>
    </div>

  </main>
</template>

<script>
export default {
  name: "StudentView",
  computed: {
    selectedStudent() {
      return this.$store.getters['students/getStudentById'](this.$route.params.id)
    }
  },
  methods: {
    remove(studentId) {
      console.log(studentId)
      this.$store.dispatch('students/removeStudent', { id: studentId })
      this.$router.push('/students')
    }
  }
}
</script>

<style scoped>

</style>