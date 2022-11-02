<template>
  <main class="container mt-4">

    <h4 class="mb-3">Add a new student</h4>

    <student-form @save-data="saveData">Add</student-form>

  </main>
</template>

<script>
import StudentForm from "@/components/students/StudentForm";

export default {
  name: "StudentAdd",
  components: {
    StudentForm
  },
  methods: {
    saveData(data) {
      this.$store.dispatch('students/addNewStudent', data.formData)
      this.$router.push('/students')
    }
  }
}
</script>

<style scoped>

</style>