<template>
  <form @submit.prevent="submitForm" class="needs-validation" novalidate>

    <hr class="mb-4">

    <div class="mb-3 row">
      <label for="firstName" class="col-sm-2 col-form-label">First name</label>
      <div class="col-sm-10">
        <input type="text" :class="firstName.classForInput" id="firstName" v-model.trim="firstName.value"/>
      </div>
      <div :class="firstName.classForFeedback">
        Valid first name is required.
      </div>
    </div>

    <div class="mb-3 row">
      <label for="lastName" class="col-sm-2 col-form-label">Last name</label>
      <div class="col-sm-10">
        <input type="text" :class="lastName.classForInput" id="lastName" v-model.trim="lastName.value" />
      </div>
      <div :class="lastName.classForFeedback">
        Valid last name is required.
      </div>
    </div>

    <div class="mb-3 row">
      <label for="email" class="col-sm-2 col-form-label">Email</label>
      <div class="col-sm-10">
        <input type="email" :class="email.classForInput" id="email" v-model="email.value" />
      </div>
      <div :class="email.classForFeedback">
        Please enter a valid email address.
      </div>
    </div>

    <div class="mb-3 row">
      <label for="phone" class="col-sm-2 col-form-label">Phone</label>
      <div class="col-sm-10">
        <input type="text" :class="phone.classForInput" id="phone" v-model="phone.value" placeholder="(999) 999-9999" @keyup="formatPhoneNumber" />
      </div>
      <div :class="phone.classForFeedback">
        Please enter a valid phone number. An example: (999) 999-9999
      </div>
    </div>

    <div class="mb-3 row">
      <label for="birth" class="col-sm-2 col-form-label">Date of Birth</label>
      <div class="col-sm-10">
        <Datepicker
            v-model="dateOfBirth.value"
            inputFormat="dd/MM/yyyy"
            :class="dateOfBirth.classForInput"
            @update:modelValue="formatDate"
        ></Datepicker>
      </div>
      <div :class="dateOfBirth.classForFeedback">
        Date of birth required. An example: 01/01/2000
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
    <p v-if="!formIsValid" >Please fix the above errors and submit again.</p>
    <div class="mb-5">
      <button class="btn btn-primary"><slot></slot></button>
      <router-link to="/students" class="btn btn-outline-primary mx-2">Back to list</router-link>
    </div>

  </form>
</template>

<script>
import Datepicker from "vue3-datepicker";

export default {
  name: "StudentAdd",
  components: {
    Datepicker
  },
  props: ['student'],
  data() {
    return {
      firstName: {
        value: '',
        isValid: true,
        classForInput: 'form-control',
        classForFeedback: 'valid'
      },
      lastName: {
        value: '',
        isValid: true,
        classForInput: 'form-control',
        classForFeedback: 'valid'
      },
      dateOfBirth: {
        value: new Date(),
        formattedDate: '',
        isValid: true,
        classForInput: 'form-control',
        classForFeedback: 'valid'
      },
      email: {
        value: '',
        isValid: true,
        classForInput: 'form-control',
        classForFeedback: 'valid'
      },
      phone: {
        value: '',
        isValid: true,
        classForInput: 'form-control',
        classForFeedback: 'valid'
      },
      checkedSports: [],
      formIsValid: true
    }
  },
  methods: {
    validateDate(date) {
      const regexForDate = new RegExp('^(0?[1-9]|[12][0-9]|3[01])[\\/](0?[1-9]|1[012])[\\/\\-]\\d{4}$')
      return regexForDate.test(date);
    },
    validateEmail(email) {
      const regexForEmail = new RegExp('^(([^<>()[\\]\\\\.,;:\\s@"]+(\\.[^<>()[\\]\\\\.,;:\\s@"]+)*)|(".+"))@((\\[[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\])|(([a-zA-Z\\-0-9]+\\.)+[a-zA-Z]{2,}))$')
      return regexForEmail.test(email);
    },
    validatePhoneNumber(phoneNumber) {
      const regexForPhoneNumber = new RegExp('[(](\\d{3})[)][ ](\\d{3})[-](\\d{4})')
      return regexForPhoneNumber.test(phoneNumber) && phoneNumber.length === 14;
    },
    formatPhoneNumber() {
      var number = this.phone.value.replace(/\D/g, '').match(/(\d{0,3})(\d{0,3})(\d{0,4})/)
      this.phone.value = '(' +number[1] + ') '+ number[2] + '-' + number[3]
    },
    formatDate(date) {
      const getRid = date.getTimezoneOffset() * 60 * 1000
      const formattedDate = new Date(date - getRid).toISOString().split('T')[0].split('-')
      this.dateOfBirth.formattedDate = formattedDate[2] + '/' + formattedDate[1] + '/' + formattedDate[0]
    },
    validateForm() {
      this.formIsValid = true

      if (this.firstName.value !== '' && this.firstName.value.length > 2) {
        this.firstName.classForInput = 'form-control is-valid'
        this.firstName.classForFeedback = 'valid'
      } else {
        this.firstName.isValid = false
        this.formIsValid = false
        this.firstName.classForInput = 'form-control is-invalid'
        this.firstName.classForFeedback = 'invalid'
      }

      if (this.lastName.value !== '' && this.lastName.value.length > 2) {
        this.lastName.classForInput = 'form-control is-valid'
        this.lastName.classForFeedback = 'valid'
      } else {
        this.lastName.isValid = 'invalid'
        this.formIsValid = false
        this.lastName.classForInput = 'form-control is-invalid'
        this.lastName.classForFeedback = 'invalid'
      }

      if (this.validateDate(this.dateOfBirth.formattedDate)) {
        this.dateOfBirth.classForInput = 'form-control is-valid'
        this.dateOfBirth.classForFeedback = 'valid'
      } else {
        this.dateOfBirth.isValid = 'invalid'
        this.formIsValid = false
        this.dateOfBirth.classForInput = 'form-control is-invalid'
        this.dateOfBirth.classForFeedback = 'invalid'
      }

      if (this.validateEmail(this.email.value)) {
        this.email.classForInput = 'form-control is-valid'
        this.email.classForFeedback = 'valid'
      } else {
        this.email.isValid = 'invalid'
        this.formIsValid = false
        this.email.classForInput = 'form-control is-invalid'
        this.email.classForFeedback = 'invalid'
      }

      if (this.validatePhoneNumber(this.phone.value)) {
        this.phone.classForInput = 'form-control is-valid'
        this.phone.classForFeedback = 'valid'
      } else {
        this.phone.isValid = 'invalid'
        this.formIsValid = false
        this.phone.classForInput = 'form-control is-invalid'
        this.phone.classForFeedback = 'invalid'
      }
    },
    submitForm() {
      this.validateForm()

      if(!this.formIsValid) {
        return
      }

      const formData = {
        firstName: this.firstName.value,
        lastName: this.lastName.value,
        dateOfBirth: this.dateOfBirth.formattedDate,
        email: this.email.value.toLowerCase(),
        phone: this.phone.value,
        favoriteSports: this.checkedSports
      }

      this.$emit('save-data', formData);
    }
  },
  created() {
    if (this.student) {
      const dateParts = this.student.dateOfBirth.split("/")
      this.dateOfBirth.value = new Date(+dateParts[2], dateParts[1] - 1, +dateParts[0])
      this.dateOfBirth.formattedDate = this.student.dateOfBirth
      this.firstName.value = this.student.firstName
      this.lastName.value = this.student.lastName
      this.email.value = this.student.email
      this.phone.value = this.student.phone
      this.checkedSports = this.student.favoriteSports
    }
  }
}
</script>

<style scoped>

</style>