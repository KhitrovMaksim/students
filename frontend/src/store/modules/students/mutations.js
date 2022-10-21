export default {
    addStudent(state, newStudent) {
        state.students.push(newStudent)
    },
    deleteStudent(state, studentToBeRemoved) {
        const indexOfStudentInStudents = state.students.map(student => student.id).indexOf(studentToBeRemoved.id);
        state.students.splice(indexOfStudentInStudents, 1)
    },
    editStudent(state, updatedStudent) {
        const indexOfStudentInStudents = state.students.map(student => student.id).indexOf(updatedStudent.id);
        state.students.splice(indexOfStudentInStudents, 1, updatedStudent)
    },
    removeAll(state) {
        state.students = []
    },
    addStudents(state, students) {
        state.students.push(...students)
    }
};