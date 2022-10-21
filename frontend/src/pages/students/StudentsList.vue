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

    <div class="table-responsive-lg">
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
        <tr v-for="student in getStudents" :key="student.id">
          <td>{{ student.id }}</td>
          <td>{{ student.firstName }}</td>
          <td>{{ student.lastName }}</td>
          <td>{{ student.dateOfBirth }}</td>
          <td>{{ student.email }}</td>
          <td>{{ student.phone }}</td>

          <td v-if="student.favoriteSports.length < 2">
            {{ student.favoriteSports[0] }}
          </td>

          <td v-else>
            {{ student.favoriteSports[0] }}...
            <Popper>
              <font-awesome-icon icon="fa-solid fa-chevron-down" />
              <template #content>
                <ul class="list-group">
                  <li v-for="sports in student.favoriteSports" :key="sports" class="list-group-item">
                    {{ sports }}
                  </li>
                </ul>
              </template>
            </Popper>
          </td>

          <td>
            <router-link :to="`/students/${student.id}`" class="btn btn-outline-info">
              <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
            </router-link>
            <router-link :to="`/students/${student.id}/edit`" class="btn btn-outline-warning mx-2">
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
  computed: {
    getStudents() {
      return this.$store.getters['students/students']
    },
    hasStudents() {
      return this.$store.getters['students/hasStudents']
    }
  },
  methods: {
    remove(studentId) {
      this.$store.dispatch('students/removeStudent', { id: studentId })
    }
  }
}
</script>

<style scoped>

</style>