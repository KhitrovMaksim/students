<template>
  <main class="container mt-4">
    <nav class="navbar navbar-expand my-3">
      <div class="container-fluid">
        <h2>List of Students</h2>
        <router-link to="/add" class="btn btn-warning">
          Add new student
        </router-link>
      </div>
    </nav>

    <div class="table-responsive">
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
          <td v-if="student.favoriteSports.length < 2">{{ student.favoriteSports[0] }}</td>
          <td v-else>
            <Popper>
              {{ student.favoriteSports[0] }}...
              <font-awesome-icon icon="fa-regular fa-square-caret-down" />
              <template>
                <ul>
                  <li v-for="sports in student.favoriteSports" :key="sports">{{ sports }}</li>
                </ul>
              </template>
            </Popper>
          </td>
          <td>
            <router-link :to="`/students/${student.id}`" class="link-secondary">
              <font-awesome-icon icon="fa-solid fa-pen" />
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
:deep(.popper) {
  background: #fff;
  border-radius: 10px;
}

:deep(.popper #arrow::before) {
  background: #fff;
}

:deep(.popper:hover),
:deep(.popper:hover > #arrow::before) {
  background: #fff;
}
</style>