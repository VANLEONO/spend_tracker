import { useParams } from "@solidjs/router";
import { createEffect, ParentProps } from "solid-js";

export default (props: ParentProps) => {
  const params = useParams()
  createEffect(() => {
    console.log(params.budgetId)
  })
  return (
    <div>
      {props.children}
    </div>
  );
}