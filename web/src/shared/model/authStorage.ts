import { LsServise } from '@shared/utils/localStorageService';

const JWT_AUTH_KEY = 'jwt_auth';
export interface JwtAuthParams {
  access: string;
  refresh: string;
  verifier: string;
  state: string;
  returnUrl: string;
}
export const authStorage = {
  setJwtAuthParams(value: Partial<JwtAuthParams>): Promise<Partial<JwtAuthParams>> {
    return LsServise.add(JWT_AUTH_KEY, value);
  },
  getJwtAuthParams(): JwtAuthParams | undefined {
    return LsServise.get<JwtAuthParams, 'sync'>(JWT_AUTH_KEY, { parse: true, type: 'sync' });
  },
  cleanJwtAuthParams() {
    return LsServise.delete(JWT_AUTH_KEY, { returning: false });
  },
};
