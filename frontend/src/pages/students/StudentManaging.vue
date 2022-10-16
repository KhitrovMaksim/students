<template>

  <main class="container mt-4">

    <h4 class="mb-3">Student</h4>

    <form>
      <hr class="mb-4">
      <div class="mb-3 row">
        <label for="firstName" class="col-sm-2 col-form-label">First name</label>
        <div class="col-sm-10">
          <input type="text" class="form-control" id="firstName">
        </div>
        <div class="invalid-feedback">
          Valid first name is required.
        </div>
      </div>

      <div class="mb-3 row">
        <label for="lastName" class="col-sm-2 col-form-label">Last name</label>
        <div class="col-sm-10">
          <input type="text" class="form-control" id="lastName">
        </div>
        <div class="invalid-feedback">
          Valid last name is required.
        </div>
      </div>

      <div class="mb-3 row">
        <label for="email" class="col-sm-2 col-form-label">Email</label>
        <div class="col-sm-10">
          <input type="email" class="form-control" id="email" placeholder="you@example.com">
        </div>
        <div class="invalid-feedback">
          Please enter a valid email address.
        </div>
      </div>

      <div class="mb-3 row">
        <label for="phone" class="col-sm-2 col-form-label">Phone</label>
        <div class="col-sm-10">
          <input type="text" class="form-control" id="phone" placeholder="">
        </div>
        <div class="invalid-feedback">
          Please enter a valid phone number.
        </div>
      </div>

      <div class="mb-3 row">
        <label for="birth" class="col-sm-2 col-form-label">Date of Birth</label>
        <div class="col-sm-10">
          <input type="date" class="form-control" id="birth">
        </div>
        <div class="invalid-feedback">
          Date of birth required
        </div>
      </div>

      <div class="mb-3 text-center">
        <div class="form-check form-check-inline">
          <input type="checkbox" class="form-check-input" id="football">
          <label class="form-check-label" for="football">Football</label>
        </div>

        <div class="form-check form-check-inline">
          <input type="checkbox" class="form-check-input" id="cricket">
          <label class="form-check-label" for="cricket">Cricket</label>
        </div>

        <div class="form-check form-check-inline">
          <input type="checkbox" class="form-check-input" id="hockey">
          <label class="form-check-label" for="hockey">Hockey</label>
        </div>

        <div class="form-check form-check-inline">
          <input type="checkbox" class="form-check-input" id="tennis">
          <label class="form-check-label" for="tennis">Tennis</label>
        </div>

        <div class="form-check form-check-inline">
          <input type="checkbox" class="form-check-input" id="golf">
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
  props: ["id", "firstName", "lastName", "dateOfBirth", "email", "phone", "favoriteSports"]
}
</script>

<style scoped>

</style>