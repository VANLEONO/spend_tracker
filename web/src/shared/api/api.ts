import Cookies from 'js-cookie';
import axios from 'axios';
import { authStorage } from '@shared/model/authStorage';

//TODO
export const api = axios;

api.interceptors.request.use(config => {
  if (config.headers) {
    if (!config.headers.Accept) {
      config.headers.Accept = 'application/json';
    }

    if (!config.headers['Content-Type']) {
      config.headers['Content-Type'] = 'application/json';
    }


    const authParams = authStorage.getJwtAuthParams();
    if (authParams?.access) {
      config.headers.Authorization = `Bearer ${authParams.access}`;
    }

    const csrftoken = Cookies.get('csrftoken');
    if (csrftoken) {
      config.headers['X-CSRFToken'] = csrftoken;
    }
  }

  return config;
});
