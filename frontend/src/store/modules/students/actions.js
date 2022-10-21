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
    },
    addTwenty(context) {
        const studentsData = [
            {
                id: '1',
                firstName: 'Maksim',
                lastName: 'Khitrov',
                dateOfBirth: '24/06/1985',
                email: 'khitrov.maksim@reqres.in',
                phone: '(111) 111-1111',
                favoriteSports: ['Football', 'Tennis']
            },
            {
                id: '2',
                firstName: 'Michael',
                lastName: 'Lawson',
                dateOfBirth: '12/10/1970',
                email: 'michael.lawson@reqres.in',
                phone: '(999) 999-9999',
                favoriteSports: ['Golf']
            },
            {
                id: '3',
                firstName: 'Michael',
                lastName: 'Lawson',
                dateOfBirth: '12/10/1970',
                email: 'michael.lawson@reqres.in',
                phone: '(999) 999-9999',
                favoriteSports: ['Golf']
            },
            {
                id: '4',
                firstName: 'Michael',
                lastName: 'Lawson',
                dateOfBirth: '12/10/1970',
                email: 'michael.lawson@reqres.in',
                phone: '(999) 999-9999',
                favoriteSports: ['Golf']
            },
            {
                id: '5',
                firstName: 'Michael',
                lastName: 'Lawson',
                dateOfBirth: '12/10/1970',
                email: 'michael.lawson@reqres.in',
                phone: '(999) 999-9999',
                favoriteSports: ['Golf']
            },
            {
                id: '6',
                firstName: 'Michael',
                lastName: 'Lawson',
                dateOfBirth: '12/10/1970',
                email: 'michael.lawson@reqres.in',
                phone: '(999) 999-9999',
                favoriteSports: ['Golf']
            },
            {
                id: '7',
                firstName: 'Michael',
                lastName: 'Lawson',
                dateOfBirth: '12/10/1970',
                email: 'michael.lawson@reqres.in',
                phone: '(999) 999-9999',
                favoriteSports: ['Golf']
            },
            {
                id: '8',
                firstName: 'Michael',
                lastName: 'Lawson',
                dateOfBirth: '12/10/1970',
                email: 'michael.lawson@reqres.in',
                phone: '(999) 999-9999',
                favoriteSports: ['Golf']
            },
            {
                id: '9',
                firstName: 'Michael',
                lastName: 'Lawson',
                dateOfBirth: '12/10/1970',
                email: 'michael.lawson@reqres.in',
                phone: '(999) 999-9999',
                favoriteSports: ['Golf']
            },
            {
                id: '10',
                firstName: 'Michael',
                lastName: 'Lawson',
                dateOfBirth: '12/10/1970',
                email: 'michael.lawson@reqres.in',
                phone: '(999) 999-9999',
                favoriteSports: ['Golf']
            }]

        context.commit('addStudents', studentsData)
    }
};