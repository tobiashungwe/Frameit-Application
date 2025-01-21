import React, { useState } from "react";
import { TextField, Typography, MenuItem, Box, Button } from "@mui/material";
import Grid from "@mui/material/Grid";
import GroupManagerModal from "./GroupManagerModal";
import TerrainManagerModal from "./TerrainManagerModal";
import MaterialManagerModal from "./MaterialManagerModal";

const ParameterSelector = ({
  groupCount,
  setGroupCount,
  terrain,
  setTerrain,
  material,
  setMaterial,
  staticGroups,
  staticTerrains,
  staticMaterials,
  t,
}) => {
  const [openGroupModal, setOpenGroupModal] = useState(false);
  const [openTerrainModal, setOpenTerrainModal] = useState(false);
  const [openMaterialModal, setOpenMaterialModal] = useState(false);

  return (
    <>
      <Grid container spacing={2} mt={2}>
        <Grid item xs={12} md={6}>
          <Typography variant="h6">{t("labels.groups")}</Typography>
          <TextField
            select
            value={groupCount}
            onChange={(e) => setGroupCount(e.target.value)}
            label={t("placeholders.select_groups")}
            fullWidth
          >
            {staticGroups.map((group) => (
              <MenuItem key={group} value={group}>
                {group}
              </MenuItem>
            ))}
          </TextField>
          {/* Button to open the "Manage Groups" popup */}
          <Button variant="outlined" onClick={() => setOpenGroupModal(true)} sx={{ mt: 1 }}>
            Manage Groups
          </Button>
        </Grid>

        <Grid item xs={12} md={6}>
          <Typography variant="h6">{t("labels.terrain")}</Typography>
          <TextField
            select
            value={terrain}
            onChange={(e) => setTerrain(e.target.value)}
            label={t("placeholders.select_terrain")}
            fullWidth
          >
            {staticTerrains.map((trn) => (
              <MenuItem key={trn} value={trn}>
                {trn}
              </MenuItem>
            ))}
          </TextField>
          <Button variant="outlined" onClick={() => setOpenTerrainModal(true)} sx={{ mt: 1 }}>
            Manage Terrains
          </Button>
        </Grid>
      </Grid>

      <Box mt={2}>
        <Typography variant="h6">{t("labels.materials")}</Typography>
        <TextField
          select
          value={material}
          onChange={(e) => setMaterial(e.target.value)}
          label={t("placeholders.select_material")}
          fullWidth
        >
          {staticMaterials.map((mat) => (
            <MenuItem key={mat} value={mat}>
              {mat}
            </MenuItem>
          ))}
        </TextField>
        <Button variant="outlined" onClick={() => setOpenMaterialModal(true)} sx={{ mt: 1 }}>
          Manage Materials
        </Button>
      </Box>

      {/*  Modals  */}
      <GroupManagerModal
        open={openGroupModal}
        onClose={() => setOpenGroupModal(false)}
      />
      <TerrainManagerModal
        open={openTerrainModal}
        onClose={() => setOpenTerrainModal(false)}
      />
      <MaterialManagerModal
        open={openMaterialModal}
        onClose={() => setOpenMaterialModal(false)}
      />
    </>
  );
};

export default ParameterSelector;
