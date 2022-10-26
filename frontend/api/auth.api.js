import api from './config.js'
import apiHelpers from './helpers.js'

export default {
  signup: (payload) => {
    return new Promise((resolve, reject) => {
      api
        .post('/api/signup', apiHelpers.dataToForm({ payload }))
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  login: (username, password) => {
    return new Promise((resolve, reject) => {
      api
        .post('/api/login', apiHelpers.dataToForm({ username, password }))
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  logout: () => {
    return new Promise((resolve, reject) => {
      api
        .post('/api/logout')
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  }
}
