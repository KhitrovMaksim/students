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
    }
};