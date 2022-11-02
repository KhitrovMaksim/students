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
    saveData(data) {
      this.$store.dispatch('students/updateStudent', {
        studentId: data.id,
        updatedStudent: data.formData
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