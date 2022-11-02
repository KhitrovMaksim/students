<template>
  <main class="container pb-5">

    <nav class="navbar navbar-expand my-3">
      <div class="container-fluid">
        <h2>List of Students</h2>
        <router-link to="/add" class="btn btn-warning">
          Add a new student
        </router-link>
      </div>
    </nav>

    <div v-if="isLoading" class="text-center">
      <div class="spinner-border" role="status">
        <span class="sr-only">Loading...</span>
      </div>
    </div>

    <div v-else class="table-responsive-lg">
      <table class="table table-sm table-hover">

        <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">First Name</th>
          <th scope="col">Last Name</th>
          <th scope="col">Date of Birth</th>
          <th scope="col">Email Address</th>
          <th scope="col">Phone Number</th>
          <th scope="col">Favorite sports</th>
          <th scope="col"></th>
        </tr>
        </thead>

        <tbody v-if="hasStudents">
        <tr v-for="(student, index) in getStudents" :key="student.id">
          <td>{{ index }}</td>
          <td>{{ student.first_name }}</td>
          <td>{{ student.last_name }}</td>
          <td>{{ student.date_of_birth }}</td>
          <td>{{ student.email }}</td>
          <td>{{ student.phone }}</td>

          <td v-if="student.favorite_sports.split(', ').length < 2">
            {{ student.favorite_sports.split(', ')[0] }}
          </td>

          <td v-else>
            {{ student.favorite_sports.split(', ')[0] }}...
            <Popper>
              <font-awesome-icon icon="fa-solid fa-chevron-down" />
              <template #content>
                <ul class="list-group">
                  <li v-for="sports in student.favorite_sports.split(', ')" :key="sports" class="list-group-item">
                    {{ sports }}
                  </li>
                </ul>
              </template>
            </Popper>
          </td>

          <td>
            <router-link :to="`/students/${index}`" class="btn btn-outline-info">
              <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
            </router-link>
            <router-link :to="`/students/${index}/edit`" class="btn btn-outline-warning mx-2">
              <font-awesome-icon icon="fa-solid fa-pen-to-square" />
            </router-link>
            <button class="btn btn-outline-danger" @click="remove(student.id)">
              <font-awesome-icon icon="fa-solid fa-trash-can" />
            </button>
          </td>

        </tr>
        </tbody>

        <caption v-else class="mt-4">
          There are no students on this list.
        </caption>

      </table>
    </div>
  </main>
</template>

<script>
import Popper from "vue3-popper";

export default{
  name: "StudentList",
  components: {
    Popper
  },
  data() {
    return {
      isLoading: false
    }
  },
  computed: {
    getStudents() {
      return this.$store.getters['students/students']
    },
    hasStudents() {
      return this.$store.getters['students/hasStudents']
    }
  },
  created() {
    this.getStudentsFromDB()
  },
  methods: {
    remove(studentId) {
      this.$store.dispatch('students/removeStudent', { id: studentId })
    },
    async getStudentsFromDB() {
      this.isLoading = true
      await this.$store.dispatch('students/getStudents')
      this.isLoading = false
    }
  }
}
</script>

<style scoped>

</style>