### Broadlink-API
- Broadlink API for house to use without Internet

[Broadlink lib guide](https://github.com/mjg59/python-broadlink)
[Broadlink control guide](https://github.com/thachnb85/control-code-for-broadlink-rm-pro/blob/master/README.md)

### Test IR codes

```python
# Enter to learning mode
device.enter_learning()

# Perform needable action
# Get IR code of action
data = device.check_data()

# Send IR code to check it work
device.send_data(data)
```