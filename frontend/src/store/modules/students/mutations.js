export default {
    addStudent(state, payload) {
        state.students.push(payload)
    },
    deleteStudent(state, payload) {
        state.students.splice(payload.id, 1)
    }
};