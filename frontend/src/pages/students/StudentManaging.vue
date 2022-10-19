<template>

  <main class="container mt-4">

    <h4 class="mb-3">Student</h4>

    <form>
      <hr class="mb-4">
      <div class="mb-3 row">
        <label for="firstName" class="col-sm-2 col-form-label">First name</label>
        <div class="col-sm-10">
          <input type="text" class="form-control" id="firstName" :placeholder="firstName" v-bind="firstName">
        </div>
        <div class="invalid-feedback">
          Valid first name is required.
        </div>
      </div>

      <div class="mb-3 row">
        <label for="lastName" class="col-sm-2 col-form-label">Last name</label>
        <div class="col-sm-10">
          <input type="text" class="form-control" id="lastName" :placeholder="lastName" v-bind="lastName">
        </div>
        <div class="invalid-feedback">
          Valid last name is required.
        </div>
      </div>

      <div class="mb-3 row">
        <label for="email" class="col-sm-2 col-form-label">Email</label>
        <div class="col-sm-10">
          <input type="email" class="form-control" id="email" :placeholder="email" v-bind="email">
        </div>
        <div class="invalid-feedback">
          Please enter a valid email address.
        </div>
      </div>

      <div class="mb-3 row">
        <label for="phone" class="col-sm-2 col-form-label">Phone</label>
        <div class="col-sm-10">
          <input type="text" class="form-control" id="phone" :placeholder="phone" v-bind="phone">
        </div>
        <div class="invalid-feedback">
          Please enter a valid phone number.
        </div>
      </div>

      <div class="mb-3 row">
        <label for="birth" class="col-sm-2 col-form-label">Date of Birth</label>
        <div class="col-sm-10">
          <input :type="type" class="form-control" id="birth" :placeholder="dateOfBirth" onfocus="(this.type='date')" onblur="(this.type='text')" v-bind="dateOfBirth">
        </div>
        <div class="invalid-feedback">
          Date of birth required
        </div>
      </div>

      <div class="mb-3 text-center">
        <div class="form-check form-check-inline">
          <input type="checkbox" class="form-check-input" id="football" value="Football" v-model="checkedSports">
          <label class="form-check-label" for="football">Football</label>
        </div>

        <div class="form-check form-check-inline">
          <input type="checkbox" class="form-check-input" id="cricket" value="Cricket" v-model="checkedSports">
          <label class="form-check-label" for="cricket">Cricket</label>
        </div>

        <div class="form-check form-check-inline">
          <input type="checkbox" class="form-check-input" id="hockey" value="Hockey" v-model="checkedSports">
          <label class="form-check-label" for="hockey">Hockey</label>
        </div>

        <div class="form-check form-check-inline">
          <input type="checkbox" class="form-check-input" id="tennis" value="Tennis" v-model="checkedSports">
          <label class="form-check-label" for="tennis">Tennis</label>
        </div>

        <div class="form-check form-check-inline">
          <input type="checkbox" class="form-check-input" id="golf" value="Golf" v-model="checkedSports">
          <label class="form-check-label" for="golf">Golf</label>
        </div>
      </div>

      <hr class="mb-4">

      <div class="text-end">
        <button type="button" class="btn btn-primary me-2">Save</button>
        <router-link to="/students" class="btn btn-warning me-2 text-white">Cancel</router-link>
        <button type="button" class="btn btn-danger">Delete</button>
      </div>

    </form>
  </main>
</template>

<script>
export default {
  name: "StudentManaging",
  props: ["id"],
  data() {
    return {
      selectedStudent: null,
      type: "text",
      checkedSports: [],
      firstName: '',
      lastName: '',
      dateOfBirth: '',
      email: '',
      phone: ''
    }
  },
  created() {
    this.selectedStudent = this.$store.getters['students/students'].find(student => student.id === this.id)
    this.checkedSports = this.selectedStudent.favoriteSports

  }
}
</script>

<style scoped>

</style>