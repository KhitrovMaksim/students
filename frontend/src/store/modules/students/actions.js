import axios from "axios";

function getLink() {
    if (window.location.host === '127.0.0.1:8080' || window.location.host === 'localhost:8080')
        return "http://localhost:8000/students/"
    return window.location.protocol + "//" + window.location.host + ":8080/students/"
}

export default {
    async addNewStudent({dispatch}, data) {
        await axios.post(getLink(), data)
        await dispatch('getStudents');
    },
    async updateStudent({dispatch}, data) {
        await axios.put(getLink() + data.studentId, data.updatedStudent)
        await dispatch('getStudents');
    },
    async removeStudent({dispatch}, studentId) {
        await axios.delete(getLink() + studentId.id)
        await dispatch('getStudents');
    },
    async removeAllStudents({dispatch}) {
        await axios.delete(getLink())
        await dispatch('getStudents');
    },
    async getStudents(context) {
        const responseData = await axios.get(getLink())
        context.commit('setStudents', responseData.data)
    },
    addSomeStudent({ dispatch }) {
        const studentsData = {
                first_name: 'Michael',
                last_name: 'Lawson',
                date_of_birth: '12/10/1970',
                email: 'michael.lawson@reqres.in',
                phone: '(999) 999-9999',
                favorite_sports: ['Golf']
        }

        dispatch("addNewStudent", studentsData)
    }
};