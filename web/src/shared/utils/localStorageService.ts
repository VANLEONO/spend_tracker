import { safeJson } from '@shared/utils/safeJSON';

export const LsServise = {
  async add<Value>(key: string, value: Value) {
    localStorage.setItem(key, getSafeValue(value));

    return value;
  },

  /**
   * @summary Функция для безопасного получения данных из local storage
   * @param key Уникальный ключ в local storage
   * @param options Указать parse = true если нужно распарсить из json
   * @returns Значение тип Result generic
   */
  get<Result, T extends 'sync' | 'async' = 'async'>(
    key: string,
    options: { parse?: boolean; type: T } = { parse: false, type: 'async' as T },
  ): T extends 'async' ? Promise<Awaited<Result | undefined>> : Result | undefined {
    const valueFromLs = localStorage.getItem(key);

    if (options?.parse && valueFromLs) {
      const { hasError, value: parsedValueFromLs } = safeJson.from<Result>(valueFromLs);

      if (!hasError)
        return (
          options.type === 'async'
            ? Promise.resolve(parsedValueFromLs)
            : parsedValueFromLs
        ) as never;
    }

    return (
      options.type === 'async' ? Promise.resolve(valueFromLs) : valueFromLs
    ) as never;
  },

  async delete(key: string, options = { returning: false }) {
    let valueToDelete = null;

    if (options.returning) {
      valueToDelete = await this.get<string, 'async'>(key);
    }

    localStorage.removeItem(key);

    return valueToDelete;
  },
};

function getSafeValue<Value>(value: Value) {
  return typeof value === 'string' ? value : safeJson.to(value);
}
