<template>
  <div class="jumbotron">
    <div
        class="container my-4 py-4 neon"
    >
      <h1 class="display-3">Hello, world!</h1>
      <p>This project is the solution to the task. The task has two parts:</p>
    </div>
    <div class="container">
      <div class="row">
        <div class="col-md-4">
          <h2>First part:</h2>
          <p>Create a good design with a strong validation for the fields below. Also, add a JS mask to the date of
            birth and phone number.
          </p>
          <p>
            Required Fields:
          </p>
          <ul>
            <li>First Name, [minimum three characters]</li>
            <li>Last Name, [minimum three characters]</li>
            <li>Date of Birth, [ format 01/01/2000 ]</li>
            <li>Email Address,</li>
            <li>Phone Number [ format (999) 999-9999]</li>
            <li>Favorite sports [checkbox]</li>
          </ul>

          <p><a
              class="btn btn-info"
              href="https://github.com/KhitrovMaksim/students/blob/main/frontend/src/pages/students/StudentAdd.vue"
              role="button"
          >View details at github »</a>
          </p>
        </div>
        <div class="col-md-4">
          <h2>Second part:</h2>
          <p>
            Using any programming language [PHP preferable] build a simple web-application that save information into
            the database and then manage it.
          </p>
          <p>
            Create pages to show:
          </p>
          <ul>
            <li>Add Page -> To add a student record to the database.</li>
            <li>View Page -> To Show all the records.</li>
            <li>Managing Page -> To Show all records, edit and/or delete records.</li>
          </ul>
          <p><a
              class="btn btn-info"
              href="https://github.com/KhitrovMaksim/students/tree/main/frontend/src/pages/students"
              role="button"
          >
            View details at github »</a>
          </p>
        </div>
        <div class="col-md-4">
          <h2>Conclusion:</h2>
          <p>
            To solve this problem, I decided to use frameworks that are familiar to me and have recently been gaining
            popularity, such as Vue 3 and FastAPI. I will also use a real server to implement this project.
          </p>
          <p>
            Stack:
          </p>
          <ul>
            <li>Frontend [VueJS, JavaScript]</li>
            <li>Backend [FastAPI, Python]</li>
            <li>Version control - GIT [GitHub]</li>
            <li>CI/CD [GitHub -> GitHub Actions -> Docker]</li>
            <li>Database [MySQL 8]</li>
            <li>Automatic configuration server [Ansible]</li>
          </ul>
        </div>
      </div>

      <hr>

    </div>
  </div>
</template>

<script>
export default {
  name: "About"
}
</script>

<style scoped>

</style>