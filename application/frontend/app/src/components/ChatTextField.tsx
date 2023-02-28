import React from "react";
import TextField from "@mui/material/TextField";

export const ChatTextField: React.FunctionComponent = () => {
  return (
    <div>
      <TextField
        id="outlined-multiline-flexible"
        label=""
        multiline
        maxRows={6}
      />
    </div>
  );
};
