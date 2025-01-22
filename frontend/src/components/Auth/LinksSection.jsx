import React from "react";
import { Box, Link } from "@mui/material";

const LinksSection = ({ links }) => {
  return (
    <Box sx={{ mt: 2 }}>
      {links.map((link, index) => (
        <React.Fragment key={index}>
          <Link href={link.href} underline="hover">
            {link.label}
          </Link>
          {index < links.length - 1 && <br />}
        </React.Fragment>
      ))}
    </Box>
  );
};

export default LinksSection;
