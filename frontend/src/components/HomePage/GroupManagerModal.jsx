// src/components/GroupManagerModal.jsx
import React, { useEffect, useState } from "react";
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Button,
  TextField,
  IconButton,
  List,
  ListItem,
  ListItemText,
  ListItemSecondaryAction
} from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";
import EditIcon from "@mui/icons-material/Edit";
import axios from "axios";

const GroupManagerModal = ({ open, onClose }) => {
  const [groups, setGroups] = useState([]);
  const [newGroupName, setNewGroupName] = useState("");
  const [editGroupId, setEditGroupId] = useState(null);
  const [editGroupName, setEditGroupName] = useState("");

  useEffect(() => {
    if (open) {
      fetchGroups();
    }
  }, [open]);

  const fetchGroups = async () => {
    try {
      const response = await axios.get("/api/groups");
      setGroups(response.data);
    } catch (err) {
      console.error("Failed to fetch groups", err);
    }
  };

  const handleAddGroup = async () => {
    if (!newGroupName.trim()) return;
    try {
      const response = await axios.post("/api/groups", null, {
        params: { name: newGroupName },
      });
      setNewGroupName("");
      setGroups([...groups, response.data]);
    } catch (err) {
      console.error("Failed to create group", err);
    }
  };

  const handleEditGroup = (group) => {
    setEditGroupId(group.id);
    setEditGroupName(group.name);
  };

  const handleUpdateGroup = async () => {
    try {
      const response = await axios.put(`/api/groups/${editGroupId}`, null, {
        params: { name: editGroupName },
      });
      setGroups(groups.map(g => g.id === editGroupId ? response.data : g));
      setEditGroupId(null);
      setEditGroupName("");
    } catch (err) {
      console.error("Failed to update group", err);
    }
  };

  const handleDeleteGroup = async (id) => {
    try {
      await axios.delete(`/api/groups/${id}`);
      setGroups(groups.filter(g => g.id !== id));
    } catch (err) {
      console.error("Failed to delete group", err);
    }
  };

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle>Manage Groups</DialogTitle>
      <DialogContent dividers>
        {/* Display existing groups */}
        <List>
          {groups.map((group) => (
            <ListItem key={group.id}>
              {editGroupId === group.id ? (
                <TextField
                  size="small"
                  value={editGroupName}
                  onChange={(e) => setEditGroupName(e.target.value)}
                />
              ) : (
                <ListItemText primary={group.name} />
              )}
              <ListItemSecondaryAction>
                {editGroupId === group.id ? (
                  <IconButton onClick={handleUpdateGroup} edge="end">
                    <EditIcon />
                  </IconButton>
                ) : (
                  <IconButton onClick={() => handleEditGroup(group)} edge="end">
                    <EditIcon />
                  </IconButton>
                )}
                <IconButton onClick={() => handleDeleteGroup(group.id)} edge="end">
                  <DeleteIcon />
                </IconButton>
              </ListItemSecondaryAction>
            </ListItem>
          ))}
        </List>

        {/* Add new group */}
        <TextField
          label="New Group Name"
          value={newGroupName}
          onChange={(e) => setNewGroupName(e.target.value)}
          fullWidth
          margin="dense"
        />
        <Button variant="contained" onClick={handleAddGroup} sx={{ mt: 1 }}>
          Add Group
        </Button>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose} color="primary">
          Close
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default GroupManagerModal;
