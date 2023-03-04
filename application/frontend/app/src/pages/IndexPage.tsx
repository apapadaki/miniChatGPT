import React from "react";
import { ChatTextField } from "../components/ChatTextField";
import { Menu } from "../components/Menu";

export const IndexPage: React.FunctionComponent = () => {
  return (
    <>
      <Menu conversations={["How much I love Afozitaki?", "Very much?"]} />
      <ChatTextField />
    </>
  );
};
