/* type-safe wrapper over json */
export const safeJson = {
  /* parses from string to typed value */
  from<ParsedResult = unknown, Value = unknown>(value: Value) {
    if (this.is(value)) {
      return {
        hasError: false as const,
        value: JSON.parse(value) as ParsedResult,
      };
    }

    return {
      hasError: true as const,
      value,
    };
  },

  /* turns the value into a string if it is not a string */
  to<Value = unknown>(value: Value) {
    return typeof value === 'string' ? value : JSON.stringify(value);
  },

  /* checks if the value is a valid json string */
  is: (value: unknown): value is string => {
    try {
      JSON.parse(value as string);
    } catch (e) {
      return false;
    }

    return true;
  },
};
