export default {
    addNewStudent(context, data) {
        const studentData = {
            id: '3',
            firstName: data.firstName,
            lastName: data.lastName,
            dateOfBirth: data.dateOfBirth,
            email: data.email,
            phone: data.phone,
            favoriteSports: data.favoriteSports
        }

        context.commit('addStudent', studentData)
    },
    removeStudent(context, studentId) {
        context.commit('deleteStudent', studentId)
    },
    removeAllStudents(context) {
        context.commit('removeAll')
    },
    editTheStudent(context, data) {

        const studentData = {
            id: data.studentId,
            firstName: data.updatedStudent.firstName,
            lastName: data.updatedStudent.lastName,
            dateOfBirth: data.updatedStudent.dateOfBirth,
            email: data.updatedStudent.email,
            phone: data.updatedStudent.phone,
            favoriteSports: data.updatedStudent.favoriteSports
        }

        context.commit('editStudent', studentData)
    }
};