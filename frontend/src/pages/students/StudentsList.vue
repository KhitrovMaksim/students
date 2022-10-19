<template>
  <main class="container">

    <nav class="navbar navbar-expand my-3">
      <div class="container-fluid">
        <h2>List of Students</h2>
        <router-link to="/add" class="btn btn-warning">
          Add a new student
        </router-link>
      </div>
    </nav>

    <div class="table-responsive-lg">
      <table class="table table-striped table-sm table-hover">

        <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">First Name</th>
          <th scope="col">Last Name</th>
          <th scope="col">Date of Birth</th>
          <th scope="col">Email Address</th>
          <th scope="col">Phone Number</th>
          <th scope="col">Favorite sports</th>
          <th scope="col">Edit</th>
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
            <router-link :to="`/students/${student.id}`" class="link-info">
              <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
            </router-link>
            <router-link :to="`/students/${student.id}`" class="link-secondary mx-2">
              <font-awesome-icon icon="fa-solid fa-pen-to-square" />
            </router-link>
            <router-link :to="`/students/${student.id}`" class="link-danger">
              <font-awesome-icon icon="fa-solid fa-trash-can" />
            </router-link>
          </td>

        </tr>
        </tbody>

        <tfoot v-else>
          No students
        </tfoot>

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
  }

}
</script>

<style scoped>

</style>