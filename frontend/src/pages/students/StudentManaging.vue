<template>
  <main class="container mt-4">

    <h4 class="mb-3">Edit the student</h4>

    <student-form @save-data="saveData" :student="student">Save changes</student-form>

  </main>
</template>

<script>
import StudentForm from "@/components/students/StudentForm";

export default {
  name: "StudentManaging",
  components: {
    StudentForm
  },
  methods: {
    saveData(formData) {
      this.$store.dispatch('students/editTheStudent', {
        studentId: this.$route.params.id,
        updatedStudent: formData
      })
      this.$router.push('/students')
    }
  },
  computed: {
    student() {
      return this.$store.getters['students/getStudentById'](this.$route.params.id)
    }
  }
}
</script>

<style scoped>

</style>