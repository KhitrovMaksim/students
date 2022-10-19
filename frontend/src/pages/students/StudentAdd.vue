<template>

  <main class="container">

    <h4 class="mb-3">Add a new student</h4>

    <form @submit.prevent="submitForm">
      <hr class="mb-4">
      <div class="mb-3 row">
        <label for="firstName" class="col-sm-2 col-form-label">First name</label>
        <div class="col-sm-10">
          <input type="text" class="form-control" id="firstName" v-model="firstName" />
        </div>
        <div class="invalid-feedback">
          Valid first name is required.
        </div>
      </div>

      <div class="mb-3 row">
        <label for="lastName" class="col-sm-2 col-form-label">Last name</label>
        <div class="col-sm-10">
          <input type="text" class="form-control" id="lastName" v-model="lastName">
        </div>
        <div class="invalid-feedback">
          Valid last name is required.
        </div>
      </div>

      <div class="mb-3 row">
        <label for="email" class="col-sm-2 col-form-label">Email</label>
        <div class="col-sm-10">
          <input type="email" class="form-control" id="email" v-model="email">
        </div>
        <div class="invalid-feedback">
          Please enter a valid email address.
        </div>
      </div>

      <div class="mb-3 row">
        <label for="phone" class="col-sm-2 col-form-label">Phone</label>
        <div class="col-sm-10">
          <input type="text" class="form-control" id="phone" v-model="phone">
        </div>
        <div class="invalid-feedback">
          Please enter a valid phone number.
        </div>
      </div>

      <div class="mb-3 row">
        <label for="birth" class="col-sm-2 col-form-label">Date of Birth</label>
        <div class="col-sm-10">
          <input :type="type" class="form-control" id="birth" onfocus="(this.type='date')" onblur="(this.type='text')" v-model="dateOfBirth">
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

      <div class="text-end mb-5">
        <button class="btn btn-primary">Add</button>
      </div>

    </form>
  </main>
</template>

<script>
export default {
  name: "StudentAdd",
  data() {
    return {
      type: "text",
      firstName: '',
      lastName: '',
      dateOfBirth: '',
      email: '',
      phone: '',
      checkedSports: [],
    }
  },
  methods: {
    submitForm() {
      const formData = {
        firstName: this.firstName,
        lastName: this.lastName,
        dateOfBirth: this.dateOfBirth,
        email: this.email,
        phone: this.phone,
        favoriteSports: this.checkedSports
      }

      this.$store.dispatch('students/addNewStudent', formData)
      this.$router.push('/students')
    }
  }
}
</script>

<style scoped>

</style>