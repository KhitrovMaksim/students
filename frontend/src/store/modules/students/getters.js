export default {
    students(state) {
        return state.students;
    },
    hasStudents(state) {
        return state.students && state.students.length > 0;
    },
    getStudentById: (state) => (id) => {
        return state.students[id]
    }
}